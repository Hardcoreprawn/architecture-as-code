# MVP Refocused: Architecture Chores Nobody Does

**Version:** 2.0  
**Date:** November 22, 2025  
**Target:** Enterprise/Solution/Technical Architects

---

## The Real Problem

**Architecture work is 80% boring chores:**

- Keeping inventory up-to-date (spreadsheet hell)
- Checking if anyone follows your standards (they don't)
- Writing documentation nobody reads (then it's immediately stale)
- Answering "what do we have?" for the 100th time
- Proving architecture adds value (executives don't see it)

**Security tools exist (Azure Security Center, Defender).  
Cost tools exist (Azure Cost Management, Advisor).  
But there's NO tool for architecture visibility and standards compliance.**

---

## What This MVP Does

### Automates the Boring Architecture Chores

**In 5 minutes, get answers to:**

1. **"What applications exist?"** (grouped resources by tags/RGs)
2. **"Are we following standards?"** (tag compliance, naming, landing zones)
3. **"What's documented vs. what's deployed?"** (doc-to-reality gap)
4. **"What's operationally ready?"** (backups, monitoring, runbooks)

**Output:** Markdown inventory report + per-application stubs

---

## Example Output

### Main Report: `inventory.md`

```markdown
# Architecture Inventory: prod-customer-experience
**Date:** 2025-11-22 | **Resources:** 127 | **Apps:** 5

## Summary

📊 **Applications:** 5 identified  
📝 **Documented:** 3 (60%)  
🏷️ **Tag Compliance:** 42% (need: app, env, owner, cost-center)  
⚙️ **Operational Readiness:** 60% average

## Standards Compliance Report

### Naming Conventions ✅ 85%
- Resource groups: 80% follow `rg-{app}-{env}`
- Resources: 90% follow standards
- ⚠️ 12 legacy resources don't match pattern

### Tagging Standards ⚠️ 42%
- Required tags (app, env, owner, cost-center): 42% complete
- 85 resources missing tags (67%)
- Top offenders: Storage accounts (23), VMs (18)

### Landing Zones ✅ 90%
- 90% of resources in correct subscription
- ⚠️ 5 prod resources in nonprod subscription (needs migration)

## Application Portfolio

### 1. Mobile App [DOCUMENTED ✅]
- **Resources:** 12 | **Cost:** $650/mo | **Status:** Operational
- **Tags:** 75% compliant | **Docs:** ✅ Exists (52 days old ⚠️)
- **Operational:** ⚠️ No CosmosDB backup, no runbook
- **Action:** Update docs, add backup, create runbook

### 2. Customer Portal [DOCUMENTED ✅]
- **Resources:** 8 | **Cost:** $450/mo | **Status:** Operational
- **Tags:** 90% compliant | **Docs:** ✅ Exists (10 days old ✅)
- **Operational:** ✅ Backups configured, monitoring active
- **Action:** Add runbook

### 3. Partner Portal [DOCUMENTED ✅]
- **Resources:** 7 | **Cost:** $150/mo | **Status:** DEPRECATED
- **Tags:** 100% compliant | **Docs:** ✅ Exists + sunset plan
- **Operational:** ✅ All configured (planned sunset: 2026-02-28)
- **Action:** None (sunset in progress)

### 4. Internal Reporting [NOT DOCUMENTED ❌]
- **Resources:** 18 | **Cost:** $320/mo | **Status:** Unknown
- **Tags:** 0% compliant (no tags at all!)
- **Operational:** ❌ Unknown (no monitoring configured)
- **Action:** CREATE DOCS, add tags, assess operational state

### 5. Legacy Data Migration [NOT DOCUMENTED ❌]
- **Resources:** 6 VMs | **Cost:** $180/mo | **Status:** Unknown
- **Tags:** 0% compliant
- **Operational:** ❌ Unknown
- **Action:** Find owner, document or decommission

## Quick Wins (Architecture Debt Reduction)

### This Week:
1. Tag the 85 untagged resources (2-3 hours with Azure Policy)
2. Create stub docs for 2 undocumented apps (2 hours)
3. Add CosmosDB backup to Mobile App (30 min)

### This Month:
4. Create operational runbooks for top 3 apps (3 days)
5. Migrate 5 misplaced prod resources to correct subscription (1 day)
6. Decide fate of Legacy Data Migration (document or decommission)

### This Quarter:
7. Achieve 90% tag compliance (ongoing)
8. 100% of apps documented (target: 5/5)
9. Operational readiness 90%+ across portfolio
```

### Per-Application Stubs Generated

**File:** `docs/internal-reporting.md` (auto-generated stub)

```markdown
---
title: "Internal Reporting"
status: "undocumented"
generated: 2025-11-22
needs_review: true
---

# Internal Reporting

> ⚠️ **AUTO-GENERATED STUB** - This application has no documentation. Please review and complete.

## Discovered Resources (via resource group: rg-internal-reporting-prod)

### Compute
- **App Service:** app-reporting-web-prod (P1v2, Linux, .NET 6)
- **Function App:** func-reporting-export-prod (EP1, Python 3.9)

### Data
- **SQL Database:** sql-reporting-db-prod (S2, 250GB, backups enabled ✅)

### Storage
- **Storage Account:** streportingprod (StorageV2, 450GB, LRS)

## Discovered Dependencies (Network Topology)
```

[app-reporting-web-prod] → [sql-reporting-db-prod]
[func-reporting-export-prod] → [sql-reporting-db-prod]
[func-reporting-export-prod] → [streportingprod]

```

## Standards Compliance
- ⚠️ **Tags:** NONE - Missing all required tags
- ✅ **Naming:** Follows conventions
- ✅ **Landing Zone:** Correct subscription (prod-internal-ops)

## Operational Status
- ✅ **Backup:** SQL Database has automated backups
- ❌ **Monitoring:** No Application Insights configured
- ❌ **Runbook:** No operational documentation

## NEXT STEPS (REQUIRED)

1. **Find Owner:** Who manages this application?
2. **Add Tags:** app=internal-reporting, env=prod, owner=?, cost-center=?
3. **Document Purpose:** What business function does this serve?
4. **Add Monitoring:** Configure Application Insights
5. **Create Runbook:** Deployment, troubleshooting, incident response

**Assigned to:** [Architecture Team - UNASSIGNED]  
**Due Date:** [2 weeks from scan]
```

---

## Why This Matters (For Architects)

### Problem: Architecture is Invisible

**Current state:**

- Executives don't see architecture work
- It's treated as optional bureaucracy
- You spend 80% of time on inventory/compliance chores
- Documentation is always wrong

**With this tool:**

- ✅ Show portfolio view (5 apps, X resources, Y% compliant)
- ✅ Prove progress (42% → 75% → 90% tag compliance)
- ✅ Automate inventory (5 min scan vs. 2 day spreadsheet exercise)
- ✅ Make architecture gaps visible (2 apps undocumented!)

### Problem: Nobody Follows Standards

**Current state:**

- You write standards nobody reads
- Tags missing, naming inconsistent
- No way to measure compliance
- Can't enforce at scale

**With this tool:**

- ✅ Measure compliance (42% tag compliance is bad, fix it)
- ✅ Identify violations (85 resources missing tags - here's the list)
- ✅ Track improvement (monthly scans show progress)
- ✅ Automate enforcement (combine with Azure Policy)

### Problem: Documentation is Always Wrong

**Current state:**

- Docs written once, never updated
- Reality diverges from docs in days
- Nobody reads outdated docs
- Writing docs feels pointless

**With this tool:**

- ✅ Detect staleness (docs 52 days old, deployed 37 days ago)
- ✅ Generate stubs for undocumented apps (start from reality)
- ✅ Auto-refresh resource lists (weekly scans update inventory)
- ✅ Focus human time on business context (not resource lists)

---

## What It Doesn't Do (Intentionally)

### Not Security (That's Crowded)

- ❌ Not replacing Azure Security Center
- ❌ Not finding vulnerabilities
- ❌ Not scanning for misconfigurations
- ❌ Not doing compliance checks (PCI, SOC2, etc.)

**Why:** Security teams have tools. Architects don't.

### Not Cost Optimization (That Exists)

- ❌ Not replacing Azure Cost Management
- ❌ Not finding underutilized resources
- ❌ Not doing cost forecasting

**Why:** FinOps teams have tools. We just report cost per app for context.

### Not Operations (That's Different)

- ❌ Not monitoring performance
- ❌ Not alerting on incidents
- ❌ Not replacing Application Insights

**Why:** Ops teams have tools. We check if monitoring is configured.

---

## The Architecture Gap This Fills

**What exists:**

- Security tools (Defender, Security Center)
- Cost tools (Cost Management, Advisor)
- Operations tools (Monitor, Application Insights)
- IaC tools (Terraform, Bicep)

**What's missing:**

- ✅ Application portfolio visibility
- ✅ Standards compliance measurement
- ✅ Documentation-to-reality alignment
- ✅ Architecture governance at scale

**This tool fills the architecture gap.**

---

## Success Criteria (For Architects)

**Month 1:**

- ✅ Complete portfolio inventory (know what you have)
- ✅ Baseline compliance metrics (42% tags, 60% docs)
- ✅ Identify quick wins (tag 85 resources, document 2 apps)

**Month 3:**

- ✅ 75%+ tag compliance (improvement visible)
- ✅ 80%+ apps documented (stubs completed, business context added)
- ✅ Operational readiness 75%+ (backups, monitoring, runbooks)

**Month 6:**

- ✅ 90%+ tag compliance (standards mostly followed)
- ✅ 100% apps documented (nothing undocumented)
- ✅ Weekly scans automated (stay current)
- ✅ Executives reference portfolio view in meetings

**Value Delivered:**

- Save 8 hours/week (no more manual inventory)
- Prove architecture value (metrics, trends, compliance)
- Reduce risk (operational gaps identified)
- Enable better decisions (know what you have)

---

## Implementation (5 Days → Shareable Site)

**Day 1: Core Scanner + Data Model**

- Azure Resource Graph queries (inventory)
- Group resources (by tags or resource groups)
- Check tag compliance vs. required tags
- Check naming conventions vs. regex patterns
- **Output:** JSON data model (for future dashboards)

**Day 2: Application Discovery + Metrics**

- Identify logical applications (grouping heuristics)
- Detect documentation (search for matching .md files)
- Check operational readiness (backups, monitoring, runbooks)
- Calculate compliance percentages
- **Output:** Enriched JSON with metrics

**Day 3: Markdown Generation + Git**

- Generate main inventory report (markdown with front matter)
- Generate per-application stubs (Hugo-compatible)
- Add Quick Wins section (prioritized actions)
- Commit to Git with timestamp
- **Output:** `content/inventory.md` + `content/apps/*.md` + `data/scan.json`

**Day 4: Hugo Static Site**

- Initialize Hugo site structure
- Configure theme (Docsy or Hugo Book)
- Set up front matter for navigation/search
- Local preview: `hugo serve`
- **Output:** Beautiful HTML site (localhost:1313)

**Day 5: Deploy to Azure Static Web Apps**

- Configure Azure Static Web Apps (from Git)
- Enable Entra ID authentication (enterprise SSO)
- Set up custom domain (optional)
- Auto-deploy on Git push
- **Output:** Live shareable site with enterprise auth

---

## Publishing Evolution

### Week 1-2: Markdown + Git
```bash
arch-scan --output ./arch-docs/content
cd arch-docs && git commit -m "Scan 2025-11-22"
```
**Share:** Git repo, manual copy to SharePoint

### Week 3: Static Site (Hugo)
```bash
hugo serve  # Preview at localhost:1313
git push    # Auto-deploys to staticweb.azure.com
```
**Share:** URL with Entra ID auth (enterprise SSO)

### Month 2: Interactive Dashboards
- Add Chart.js for compliance trends
- Interactive tables (sort/filter apps)
- Still markdown-based, enhanced with JavaScript

### Month 3+: API + Dynamic Queries
- Azure Static Web Apps API (serverless)
- Query historical scans
- Compare snapshots
- Export reports on-demand

---

## Roadmap (After MVP)

### Phase 1: Weekly Scans + Trend Tracking

- Automated weekly scans
- Track compliance over time
- Alert on regressions

### Phase 2: Doc Generation from Templates

- EA-on-a-Page template
- C4 diagram generation (basic)
- Auto-populate from discovered resources

### Phase 3: Integration with ADRs

- Link architecture decisions to applications
- Track decision outcomes
- Show "why" behind current state

### Phase 4: Fitness Functions

- Define target architecture
- Measure conformance
- Alert on drift from target state

---

## Related Documents

- **[ROADMAP.md](ROADMAP.md)** - Product evolution phases
- **[BUSINESS-MODEL-CANVAS.md](BUSINESS-MODEL-CANVAS.md)** - Business model (updated for architect focus)

---

**Document Owner:** Architecture Team  
**Status:** Focused on architecture gap, not security
