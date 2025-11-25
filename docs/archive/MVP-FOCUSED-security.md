# Focused MVP: Architecture Debt Report

**Version:** 2.0  
**Date:** November 22, 2025  
**Target Audience:** Enterprise/Solution/Technical Architects

---

## The Actual Problem (For Architects)

**Reality:** You're an architect, and you're drowning in chores nobody values:

- **Documentation is always outdated** - You wrote it 6 months ago, it's wrong now
- **"What resources do we have?"** - Takes 2 days to answer, spreadsheet is immediately stale
- **Nobody follows the standards** - Tags missing, naming conventions ignored, sprawl everywhere
- **Can't prove you're adding value** - Executives don't see architecture work
- **Operational concerns buried** - Which apps are at risk? Which are expensive? Nobody knows.

**The Urgent Problem:** Architecture is invisible, so it's treated as optional bureaucracy instead of essential engineering.

---

## What This MVP Actually Does (No Fluff)

### Single Purpose: Architecture Inventory + Standards Compliance

**In 5 minutes, answer the questions you hate:**

1. **"What do we have?"** - Complete inventory of resources, grouped by application
2. **"Are we following standards?"** - Tag compliance, naming conventions, landing zones alignment
3. **"What's at risk?"** - Missing backups, deprecated SKUs, operational gaps
4. **"What's documented?"** - Which apps have architecture docs, which don't (spoiler: none)

**Output:** One markdown file that architects actually want to read.

**That's it.** No security alerts (Azure Security Center does that). No AI grouping (tags work fine). Just **architecture visibility and standards compliance** - the boring stuff nobody does.

---

## How It Works (Dead Simple)

```bash
# Install
pip install azure-risk-scanner

# Run (uses your Azure CLI credentials)
az-risk-scan --subscription prod-subscription --output report.md

# Read report
cat report.md
```

**What happens:**

1. Queries Azure Resource Graph (fast, read-only, no changes)
2. Checks Azure Security Center recommendations
3. Checks Azure Advisor cost recommendations
4. Looks for resources with no tags
5. Generates markdown report

**Time:** 2-3 minutes for 500 resources  
**Permissions needed:** `Reader` role (nothing scary)  
**Side effects:** None (read-only queries)

---

## Output: The "Oh Shit" Report

```markdown
# Azure Risk Report: prod-customer-experience
**Scan Date:** 2025-11-22 14:30 UTC  
**Subscription:** prod-customer-experience (12345678-1234-1234-1234-123456789abc)  
**Resources Scanned:** 127

---

## Executive Summary

🔴 **3 CRITICAL** - Fix today  
🟠 **8 HIGH** - Fix this week  
🟡 **15 MEDIUM** - Fix this month  

**Estimated Risk:** $50K-200K potential loss (data breach or outage)  
**Estimated Waste:** $1,800/month in unnecessary spending  
**Documentation Gap:** 67% of resources have no owner tag

---

## 🔴 CRITICAL (Fix Today)

### 1. PostgreSQL Database Open to Internet

**Resource:** `psql-customer-prod` (rg-mobile-app-prod)  
**Problem:** Public network access enabled, firewall rule `0.0.0.0/0`  
**Risk:** Direct internet exposure, brute force attack risk  
**Impact:** Contains customer PII (potentially 50K+ records)

**Evidence:**
```bash
az postgres flexible-server show \
  --name psql-customer-prod \
  --resource-group rg-mobile-app-prod \
  --query "{publicAccess:publicNetworkAccess, firewallRules:firewallRules}"
# Result: publicAccess: "Enabled", firewallRules: ["AllowAll: 0.0.0.0-255.255.255.255"]
```

**Fix:**

1. Disable public access: 15 minutes
2. Enable private endpoint: 30 minutes
3. Update connection strings: 15 minutes

**Cost to fix:** $0 (private endpoints included in pricing)

---

### 2. Storage Account with Public Blob Access

**Resources:**

- `stcustomerprod` (rg-customer-portal-prod) - 450GB
- `stmobiledata` (rg-mobile-app-prod) - 1.2TB  
- `stinternalfiles` (rg-internal-ops-prod) - 89GB

**Problem:** Anonymous public read access enabled on blob containers  
**Risk:** Anyone with the URL can download files  
**Impact:** Potentially confidential documents, customer data

**Evidence:**

```bash
az storage account show --name stcustomerprod --query "allowBlobPublicAccess"
# Result: true
```

**Fix:** Disable public access (5 minutes per account, zero downtime)

---

### 3. No Backups Configured

**Resources:**

- CosmosDB: `cosmos-mobile-data-prod` (17GB) - NO BACKUP
- App Services: 5 instances - NO BACKUP
- PostgreSQL: `psql-reporting` (230GB) - NO BACKUP

**Problem:** No point-in-time restore available  
**Risk:** Accidental deletion = permanent data loss  
**Impact:** Business continuity failure, potential regulatory violation

**Evidence:**

```bash
az cosmosdb show --name cosmos-mobile-data-prod --query "backupPolicy.type"
# Result: "Periodic" with 0 retention
```

**Fix:**

- CosmosDB: Enable continuous backup ($80/month)
- App Services: Enable automated backups ($15/month each)
- PostgreSQL: Already has automatic backups (verify retention)

**Cost to fix:** ~$155/month total

---

## 🟠 HIGH PRIORITY (This Week)

### 4. Underutilized VMs Wasting Money

**Resources:** 12 VMs in nonprod-customer-experience  
**Problem:** Running 24/7 with <5% CPU average (last 30 days)  
**Cost:** $2,400/month | **Potential savings:** $1,800/month

| VM | Size | Monthly Cost | Avg CPU | Recommendation |
|----|------|--------------|---------|----------------|
| vm-dev-01 | D4s_v3 | $200 | 3% | Auto-shutdown or downsize to B2s ($30) |
| vm-dev-02 | D4s_v3 | $200 | 2% | Auto-shutdown or downsize to B2s ($30) |
| ... | ... | ... | ... | ... |

**Fix:** Enable auto-shutdown (7pm-7am + weekends) or delete unused VMs

---

### 5. TLS 1.0/1.1 Still Enabled

**Resources:** 6 App Services still allow deprecated TLS versions  
**Problem:** Compliance violation (PCI-DSS requires TLS 1.2+)  
**Risk:** Failed audit, potential compliance fine

**Fix:** 5 minutes per app service (configuration change, no code deploy needed)

---

### 6. Resources with No Owner Tag

**Count:** 85 of 127 resources (67%) have no `owner` tag  
**Problem:** Nobody knows who's responsible  
**Impact:** Can't get approvals, can't allocate costs, can't clean up

**Top offenders:**

- 23 storage accounts
- 18 VMs
- 12 NSGs
- 32 other resources

**Fix:** Tag resources with owning team (use Azure Policy to enforce going forward)

---

## 🟡 MEDIUM PRIORITY (This Month)

### 7-15. [Standard Azure Advisor Recommendations]

- No Application Insights configured (6 App Services)
- SQL DTU utilization <10% (3 databases) - downsize recommended
- Orphaned NICs (8 resources) - $5/month waste
- Orphaned disks (12 resources) - $180/month waste
- No diagnostic logs enabled (19 resources)
- Missing resource locks on production (37 resources)
- [etc...]

---

## What's Actually Documented

**Resources with Architecture Docs:** 0 / 127 (0%)  
**Resources with Tags:** 42 / 127 (33%)  
**Resources with Owner:** 42 / 127 (33%)  
**Resources with Cost-Center:** 15 / 127 (12%)

**Reality Check:** You have zero documentation. Everything is tribal knowledge.

---

## Recommended Next Steps

**This Week (Critical):**

1. Fix public PostgreSQL access (1 hour)
2. Disable public blob access on storage (30 minutes)
3. Enable CosmosDB backups ($80/month)

**This Month (High):**
4. Tag all resources with owners (1-2 days)
5. Enable auto-shutdown on dev/test VMs (save $1,800/month)
6. Update TLS settings (1 hour)

**This Quarter (Documentation):**
7. Start documenting what the hell anything does
8. Create architecture diagrams for top 5 applications
9. Set up regular scanning (weekly)

---

## How to Use This Report

**Don't:**

- ❌ File it away and forget
- ❌ Schedule a meeting to discuss the meeting about the report
- ❌ Create a 12-month roadmap
- ❌ Wait for perfect tooling

**Do:**

- ✅ Pick the top 3 critical issues
- ✅ Fix them this week
- ✅ Run the scan again next week
- ✅ Repeat until the critical list is empty

---

## Technical Details (For Implementers)

### What It Actually Queries

```python
# Azure Resource Graph queries
SECURITY_CHECKS = [
    "Resources | where type =~ 'microsoft.dbforpostgresql/flexibleservers' | where properties.publicNetworkAccess == 'Enabled'",
    "Resources | where type =~ 'microsoft.storage/storageaccounts' | where properties.allowBlobPublicAccess == true",
    "Resources | where type =~ 'microsoft.documentdb/databaseaccounts' | where properties.backupPolicy.type != 'Continuous'",
]

# Azure Security Center
SECURITY_RECOMMENDATIONS = azure_security_center.list_recommendations()

# Azure Advisor
COST_RECOMMENDATIONS = azure_advisor.list_recommendations(category="Cost")

# Tag compliance
TAGGED_RESOURCES = resources.list(filter="tagName eq 'owner'")
ALL_RESOURCES = resources.list()
compliance_rate = len(TAGGED_RESOURCES) / len(ALL_RESOURCES)
```

### What It Doesn't Do (No Scope Creep)

- ❌ No AI (just queries and thresholds)
- ❌ No automated fixes (too risky for MVP)
- ❌ No ServiceNow integration
- ❌ No multi-stakeholder workflows
- ❌ No architecture generation
- ❌ No diagram creation
- ❌ No CI/CD integration

**Why:** Keep it simple. Just identify problems. Humans fix them.

---

## Success Criteria

**MVP is successful if:**

1. ✅ Generates report in <5 minutes for 500 resources
2. ✅ Identifies at least 3 critical security issues (if they exist)
3. ✅ Identifies at least $500/month in cost waste
4. ✅ Produces report that non-technical exec can understand
5. ✅ Requires zero setup (uses existing Azure CLI auth)

**MVP has failed if:**

- ❌ Requires more than 5 minutes to run first scan
- ❌ Requires configuration files or setup wizard
- ❌ Produces false positives that erode trust
- ❌ Report is >10 pages (too much to read)

---

## What Comes After MVP (Maybe)

**If this is useful:**

1. Add ability to export to PDF for executives
2. Add scheduled scanning (GitHub Action / Azure Function)
3. Add trend tracking (risk score over time)
4. Add basic fix scripts (with human approval)
5. Add more check types (compliance, performance)

**If this isn't useful:**

- Stop. Don't build more. Find out why. Fix that first.

---

## The Cynical Truth

**What you don't need:**

- 🗑️ AI-powered intelligent grouping (just use tags, or query by resource group)
- 🗑️ Multi-stakeholder review workflows (email the report to people)
- 🗑️ Ephemeral test environments (overkill for read-only scanning)
- 🗑️ ServiceNow integration (create a ticket manually if you need to)
- 🗑️ Separate architecture repository (you have zero docs anyway)
- 🗑️ Azure Landing Zones reorganization (fix what's broken first)
- 🗑️ Change management workflow (you're not deploying changes yet)

**What you need:**

- ✅ List of problems
- ✅ Severity ranking
- ✅ Evidence (screenshots/CLI commands to verify)
- ✅ Rough fix effort estimates
- ✅ Rough cost impact

**That's it.**

---

## Implementation Plan (4 Days of Real Work)

**Day 1: Core Scanner**

- Set up Python project
- Implement Azure Resource Graph queries
- Query Security Center recommendations
- Query Advisor cost recommendations
- Output to JSON

**Day 2: Report Generator**

- Parse JSON results
- Score by severity (critical/high/medium/low)
- Generate markdown report
- Add evidence (CLI commands to verify)
- Add fix guidance

**Day 3: Testing**

- Test against real subscription
- Validate findings manually
- Fix false positives
- Add more check types if obvious gaps

**Day 4: Polish & Documentation**

- Write README
- Add CLI argument parsing
- Package as `pip install`
- Test installation on clean machine

**Total:** 32 hours of focused development

---

## Related Documents

**Ignore these for now:**

- ~~ARCHITECTURE-LIFECYCLE-TOOL.md~~ (too ambitious)
- ~~AZURE-APPROACH.md~~ (nice ideas, do later)
- ~~MVP.md~~ (1600 lines of "someday")

**Read this:**

- THIS FILE - do this first, get value in 1 week

---

## Final Reality Check

**You don't need a platform. You need a report.**

**You don't need AI. You need Azure Resource Graph queries.**

**You don't need workflow automation. You need to know what's broken.**

Build this in 4 days. Run it. Fix the critical issues. Then decide if you need anything else.

If you build all the "nice to have" stuff first, you'll spend 6 months and have nothing useful.

**Start here. Ship fast. Iterate based on actual usage.**

---

**Document Owner:** Someone who's tired of PowerPoint architecture  
**Last Updated:** November 22, 2025  
**Status:** This is what you should actually build
