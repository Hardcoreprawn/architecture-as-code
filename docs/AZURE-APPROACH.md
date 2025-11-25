# Azure-Opinionated Architecture Approach

**Version:** 1.0  
**Date:** November 22, 2025  
**Status:** Core Approach

---

## Overview

This tool takes an **opinionated view of Azure**, following Microsoft's best practices and patterns:

- **Microsoft Well-Architected Framework** - Design principles for reliability, security, cost, operations, performance
- **Azure Landing Zones** - Subscription organization model with clear boundaries
- **Infrastructure as Code** - All changes proposed through Terraform/Bicep
- **Clear Documentation** - Every change includes architecture docs and review summaries
- **Tag-Based Tracking** - Tags link Azure resources to architecture documentation

---

## Repository Structure

### Two-Repository Model

**1. Architecture Repository** (this repository)

```text
architecture-repo/
├── subscriptions/
│   ├── platform-connectivity/
│   │   └── architectures/
│   │       ├── hub-network/
│   │       ├── vpn-gateway/
│   │       └── expressroute/
│   │
│   ├── platform-identity/
│   │   └── architectures/
│   │       └── domain-controllers/
│   │
│   ├── prod-customer-experience/
│   │   └── architectures/
│   │       ├── mobile-app/
│   │       ├── customer-portal/
│   │       └── partner-portal/
│   │
│   └── prod-data-platform/
│       └── architectures/
│           ├── customer-cdp/
│           ├── analytics-warehouse/
│           └── streaming-platform/
│
├── enterprise/
│   ├── standards/
│   ├── patterns/
│   └── adrs/
│
└── change-proposals/
    └── active/
        ├── fix-mobile-backup/
        ├── migrate-legacy-vms/
        └── cost-optimization/
```

**Purpose:**

- Document what exists in Azure
- Track application lifecycle states
- Identify risks and improvement opportunities
- Propose changes with IaC code
- Track operational concerns (costs, risks, compliance)

**2. IaC Repository** (managed by existing IaC teams)

```text
iac-repo/
├── terraform/
│   ├── subscriptions/
│   │   ├── platform-connectivity/
│   │   ├── platform-identity/
│   │   ├── prod-customer-experience/
│   │   └── prod-data-platform/
│   │
│   └── modules/
│       ├── app-service/
│       ├── cosmosdb/
│       ├── virtual-network/
│       └── storage-account/
│
└── pipelines/
    ├── deploy-prod.yml
    ├── deploy-nonprod.yml
    └── validation.yml
```

**Purpose:**

- Maintain infrastructure code
- Deploy changes to Azure
- Manage pipeline configurations
- Version control IaC artifacts

**Integration Flow:**

```text
1. Architecture team discovers risk
2. AI generates fix with Terraform code
3. Architecture team reviews and creates change proposal
4. Stakeholders approve (security, service owner, operations)
5. IaC team reviews Terraform code
6. IaC team merges to their repo
7. Pipeline deploys to Azure
8. Architecture team updates documentation
```

---

## Azure Landing Zones Model

### Subscription Organization

**Management Group Hierarchy:**

```text
Azure Tenant (company.onmicrosoft.com)
│
├── MG: Landing Zones
│   │
│   ├── MG: Platform (shared infrastructure)
│   │   ├── Subscription: platform-connectivity
│   │   │   - Hub VNet, VPN Gateway, ExpressRoute, Firewall
│   │   │   - Owner: Network Team
│   │   │   - Budget: $5,000/month
│   │   │
│   │   ├── Subscription: platform-identity
│   │   │   - Entra ID Connect, Domain Controllers
│   │   │   - Owner: Identity Team
│   │   │   - Budget: $1,500/month
│   │   │
│   │   └── Subscription: platform-management
│   │       - Azure Monitor, Log Analytics, Automation
│   │       - Owner: Operations Team
│   │       - Budget: $3,000/month
│   │
│   ├── MG: Production Workloads
│   │   ├── Subscription: prod-customer-experience
│   │   │   - Customer-facing applications
│   │   │   - Owner: Product Team
│   │   │   - Budget: $15,000/month
│   │   │   - High criticality, customer impact
│   │   │
│   │   ├── Subscription: prod-data-platform
│   │   │   - Data lake, analytics, streaming
│   │   │   - Owner: Data Team
│   │   │   - Budget: $20,000/month
│   │   │   - High data classification
│   │   │
│   │   └── Subscription: prod-internal-ops
│   │       - Internal tools (finance, HR, admin)
│   │       - Owner: Internal IT
│   │       - Budget: $8,000/month
│   │       - Lower customer impact
│   │
│   └── MG: Non-Production Workloads
│       ├── Subscription: nonprod-customer-experience
│       │   - Dev, test, staging for customer apps
│       │   - Owner: Product Team
│       │   - Budget: $5,000/month
│       │
│       ├── Subscription: nonprod-data-platform
│       │   - Dev, test, staging for data platform
│       │   - Owner: Data Team
│       │   - Budget: $7,000/month
│       │
│       └── Subscription: sandbox-ephemeral
│           - Temporary test environments (auto-cleanup 4 hours)
│           - Owner: Architecture Team
│           - Budget: $2,000/month
```

### Subscription Selection Criteria

**When creating a new subscription, consider:**

| Factor | Description | Example |
|--------|-------------|---------|
| **Audience** | Who manages and consumes these resources? | Product Team, Data Team, Network Team |
| **Risk Profile** | Data classification and compliance requirements | PCI-DSS data → separate subscription |
| **Cost Tracking** | Need to track costs separately for chargeback? | Each business unit gets own subscription |
| **Blast Radius** | Isolate to limit impact of incidents | High-risk experiments → sandbox subscription |
| **Policy Requirements** | Different security or compliance needs | Production → strict policies, sandbox → relaxed |

---

## Resource Group Organization

### One Capability Per Resource Group

**Principle:** Each resource group contains resources for **one application or capability**.

**Good Examples:**

```text
✅ rg-mobile-app-prod
   - Function App (API)
   - CosmosDB (data)
   - Storage Account (blobs)
   - Application Insights (monitoring)
   → All resources for Mobile App

✅ rg-customer-portal-prod
   - App Service (web app)
   - PostgreSQL (database)
   - Redis Cache
   - Storage Account (static assets)
   → All resources for Customer Portal

✅ rg-hub-network-prod
   - Virtual Network (hub)
   - VPN Gateway
   - ExpressRoute Gateway
   - Azure Firewall
   → All resources for hub networking capability
```

**Bad Examples:**

```text
❌ rg-prod-resources
   - Mobile App resources
   - Customer Portal resources
   - Data platform resources
   → Too broad, unclear ownership

❌ rg-databases-prod
   - CosmosDB for mobile app
   - PostgreSQL for customer portal
   - SQL Database for finance system
   → Grouped by type, not capability - unclear dependencies

❌ rg-shared-prod
   - Random storage accounts
   - Some function apps
   - A few VMs
   → "Glob" resource group - technical debt accumulator
```

### Resource Group Naming Convention

```text
rg-{app-name}-{environment}

Examples:
- rg-mobile-app-prod
- rg-mobile-app-staging
- rg-customer-portal-prod
- rg-analytics-warehouse-prod
- rg-hub-network-prod
```

---

## Tagging Strategy

### Required Tags

**Every Azure resource MUST have these tags:**

| Tag | Description | Example | Used For |
|-----|-------------|---------|----------|
| `app` | Application or capability name | `mobile-app`, `customer-portal` | Linking to architecture docs |
| `env` | Environment | `prod`, `staging`, `dev`, `sandbox` | Filtering and cost allocation |
| `owner` | Team responsible for the resource | `product-team`, `data-team`, `network-team` | Accountability and approvals |
| `cost-center` | Cost center for chargeback | `CC-1234`, `CC-5678` | Financial tracking |
| `criticality` | Business criticality | `high`, `medium`, `low` | Risk prioritization |

### Optional Tags

| Tag | Description | Example | Used For |
|-----|-------------|---------|----------|
| `data-classification` | Data sensitivity | `public`, `confidential`, `restricted` | Compliance and security |
| `compliance` | Compliance requirements | `soc2`, `gdpr`, `pci-dss` | Audit tracking |
| `sunset-date` | Planned retirement date | `2026-02-28` | Lifecycle management |
| `architecture-link` | Link to architecture doc | `docs/mobile-app.md` | Direct navigation |
| `change-request` | Last change that modified this | `CHG0012360` | Change tracking |

### Tag Enforcement

**Azure Policy enforces tagging:**

```json
{
  "policyDefinitionName": "require-tags",
  "policyScope": "Management Group: Production Workloads",
  "effect": "Deny",
  "requiredTags": [
    "app",
    "env",
    "owner",
    "cost-center",
    "criticality"
  ]
}
```

**Result:** Cannot create resources without required tags.

### Tag-Based Tracking

**Architecture tool uses tags to link Azure resources to documentation:**

```bash
# Discover all resources for Mobile App
az resource list --tag app=mobile-app --query "[].{name:name, type:type, rg:resourceGroup}"

# Find all high-criticality resources
az resource list --tag criticality=high --query "[].{name:name, owner:tags.owner, app:tags.app}"

# Track costs by application
az consumption usage list --tag app=mobile-app
```

**In architecture documentation:**

```markdown
---
title: "Mobile App"
azure_tags:
  app: "mobile-app"
  env: "prod"
  owner: "product-team"
  cost-center: "CC-1234"
  criticality: "high"
---

# Mobile App Architecture

## Azure Resources (Discovered via Tags)

Resources with tag `app=mobile-app` and `env=prod`:

- **rg-mobile-app-prod** (Resource Group)
  - Function App: func-mobile-api-prod
  - CosmosDB: cosmos-mobile-data-prod
  - API Management: apim-mobile-prod
  - Storage: stmobileappprod
  - Application Insights: appi-mobile-prod
```

---

## Subscription Ownership and Cost Management

### Subscription Owner Responsibilities

Each subscription has an **owner** (a team, not an individual):

**Responsibilities:**

1. **Cost Management**
   - Monitor monthly spend
   - Approve budget increases
   - Review cost anomaly alerts
   - Allocate costs to cost centers

2. **Access Control**
   - Approve access requests
   - Review role assignments quarterly
   - Remove unused service principals

3. **Change Approvals**
   - Review proposed changes to their subscription
   - Approve or reject change requests
   - Participate in CAB (Change Advisory Board)

4. **Compliance**
   - Ensure resources meet policy requirements
   - Address compliance violations
   - Participate in audits

### Cost Tracking

**Budget Alerts per Subscription:**

```bash
# Set budget alert for prod-customer-experience
az consumption budget create \
  --budget-name "prod-customer-experience-monthly" \
  --amount 15000 \
  --time-grain Monthly \
  --subscription "prod-customer-experience" \
  --notification-enabled \
  --contact-emails "product-team@company.com"
```

**Alert Thresholds:**

- 80% of budget → Warning email to owner
- 90% of budget → Alert email to owner + finance
- 100% of budget → Critical alert, escalate to leadership

**Monthly Cost Review:**

Architecture tool generates monthly cost report per subscription:

```text
📊 COST REPORT: prod-customer-experience
Month: November 2025
Budget: $15,000 | Actual: $14,250 | Variance: -$750 (95% utilized) ✅

COST BY APPLICATION:
- Mobile App: $6,500 (46%) [Budget: $7,000] ✅
- Customer Portal: $4,500 (32%) [Budget: $5,000] ✅
- Partner Portal: $3,250 (23%) [Budget: $3,000] ⚠️ +8% over

TOP COST DRIVERS:
1. CosmosDB (cosmos-mobile-data-prod): $4,500/month
2. API Management (apim-mobile-prod): $1,800/month
3. App Service (app-customer-portal): $1,200/month

COST ANOMALIES:
- ⚠️ Partner Portal SQL Database increased 40% this month
  → Investigate query performance issue

OPTIMIZATION OPPORTUNITIES:
- 🔄 3 unused storage accounts detected ($150/month potential savings)
- 🔄 2 VMs running 24/7 with <5% CPU (resize or shutdown)
```

### Cost Allocation with Tags

**Using tags for chargeback:**

```bash
# Get costs by cost center
az consumption usage list \
  --start-date 2025-11-01 \
  --end-date 2025-11-30 \
  --query "[?tags.cost-center=='CC-1234'].{cost:pretaxCost, resource:instanceName}"

# Get costs by application
az consumption usage list \
  --start-date 2025-11-01 \
  --end-date 2025-11-30 \
  --query "[?tags.app=='mobile-app'].{cost:pretaxCost, resource:instanceName}"
```

---

## Change Management with IaC

### Principles

1. **All changes proposed via IaC** (Terraform or Bicep)
2. **Clear documentation** for every change
3. **Review summaries** for different audiences
4. **Test in ephemeral environments** before production
5. **Approval gates** at every stage

### Change Proposal Structure

```text
change-proposals/
└── fix-mobile-backup/
    ├── CHANGE-SUMMARY.md          (1-page executive summary)
    ├── SECURITY-REVIEW.md         (For security team)
    ├── SERVICE-OWNER-REVIEW.md    (For business owner)
    ├── OPERATIONS-REVIEW.md       (For deployment team)
    ├── ARCHITECTURE-DETAILS.md    (Full technical spec)
    │
    ├── iac/                       (Infrastructure code)
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    │
    ├── tests/                     (Validation tests)
    │   ├── smoke-test.sh
    │   └── validation-checklist.md
    │
    └── rollback/                  (Rollback procedure)
        ├── rollback.tf
        └── rollback-steps.md
```

### IaC Code Standards

**Terraform Standards:**

```hcl
# main.tf
terraform {
  required_version = ">= 1.5"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.80"
    }
  }
  backend "azurerm" {
    # State stored in centralized storage account
    resource_group_name  = "rg-terraform-state"
    storage_account_name = "stterraformstate"
    container_name       = "tfstate"
    key                  = "prod-customer-experience/mobile-app.tfstate"
  }
}

provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

# Enable CosmosDB continuous backup
resource "azurerm_cosmosdb_account" "mobile_data" {
  name                = "cosmos-mobile-data-prod"
  location            = azurerm_resource_group.mobile_app.location
  resource_group_name = azurerm_resource_group.mobile_app.name
  
  offer_type = "Standard"
  kind       = "GlobalDocumentDB"
  
  # Continuous backup for point-in-time restore
  backup {
    type                = "Continuous"
    tier                = "Continuous30Days"
    interval_in_minutes = 240
    retention_in_hours  = 720  # 30 days
  }
  
  # Required tags
  tags = {
    app              = "mobile-app"
    env              = "prod"
    owner            = "product-team"
    cost-center      = "CC-1234"
    criticality      = "high"
    change-request   = "CHG0012360"
    architecture-link = "subscriptions/prod-customer-experience/architectures/mobile-app/architecture.md"
  }
  
  lifecycle {
    prevent_destroy = true  # Production protection
  }
}
```

### Approval Flow with IaC Teams

**Step-by-Step:**

1. **Architecture team** generates change proposal with IaC code
2. **Stakeholders approve** business/security/operational aspects
3. **Architecture team** creates PR in IaC repository
4. **IaC team** reviews Terraform code for:
   - Code quality and standards compliance
   - State management correctness
   - Security best practices
   - Module usage and consistency
5. **IaC team** runs `terraform plan` and validates output
6. **IaC team** merges PR to IaC repo
7. **Pipeline** deploys change
8. **Architecture team** updates documentation

**Why separate repos?**

- IaC teams maintain their existing workflows
- Architecture team focuses on design and risk
- Clear ownership boundaries
- Existing IaC standards preserved
- Existing approval processes respected

---

## Alignment with Well-Architected Framework

### Five Pillars

**1. Reliability**

- Multi-region deployments for critical applications
- Backup and disaster recovery for all data stores
- Health checks and automated failover
- Resource group isolation limits blast radius

**2. Security**

- Subscription boundaries enforce security zones
- Azure Policy enforces tagging and encryption
- Managed Identity for authentication (no secrets)
- Network isolation with private endpoints

**3. Cost Optimization**

- Budget alerts per subscription
- Tag-based cost allocation
- Regular cost reviews
- Unused resource detection and cleanup

**4. Operational Excellence**

- Infrastructure as Code for all changes
- Automated deployment pipelines
- Monitoring and alerting configured
- Runbooks for operational procedures

**5. Performance Efficiency**

- Right-sizing recommendations from Azure Advisor
- Performance monitoring with Application Insights
- Load testing before production deployment
- Regular performance reviews

---

## Summary: Azure-Opinionated Approach

**This tool is opinionated about Azure:**

✅ **Use Azure Landing Zones** for subscription organization  
✅ **Follow Well-Architected Framework** for design decisions  
✅ **One capability per resource group** (no "glob" groups)  
✅ **Tag everything** for tracking and cost allocation  
✅ **All changes via IaC** (Terraform or Bicep)  
✅ **Clear documentation** with review summaries  
✅ **Subscription ownership** with budget accountability  

**Separate repos for architecture and IaC:**

- Architecture repo: Design, risk, change proposals
- IaC repo: Infrastructure code, pipelines, deployment
- Integration: Change proposals flow from architecture to IaC

**Result:** Consistent, well-architected Azure infrastructure with clear ownership and accountability.

---

## Related Documents

- **[README.md](README.md)** - Project overview
- **[ARCHITECTURE-LIFECYCLE-TOOL.md](ARCHITECTURE-LIFECYCLE-TOOL.md)** - Core concept and workflow
- **[MVP.md](MVP.md)** - Technical implementation details

---

**Document Owner:** Architecture Team  
**Last Updated:** November 22, 2025  
**Status:** Core Approach Definition
