# Architecture Visibility Platform

**Automate the boring architecture chores:** inventory, standards compliance, documentation gaps.

**Target Audience:** Enterprise/Solution/Technical Architects

**Why This Exists:** Security teams have tools (Defender, Security Center), cost teams have tools (Cost Management), operations teams have tools (Monitor, Application Insights). **Architects have spreadsheets.** This fills the architecture gap.

---

## The Problem

Architecture work is 80% boring chores:

- Keeping inventory up-to-date (spreadsheet hell)
- Checking if anyone follows standards (they don't)
- Answering "what do we have?" for the 100th time
- Proving architecture adds value (executives don't see it)
- Writing documentation that's immediately stale

**Result:** Architecture is invisible, so it's treated as optional bureaucracy.

---

## The Solution

**5-minute automated scan that generates:**

1. Application portfolio inventory (grouped resources)
2. Standards compliance report (tags, naming, landing zones)
3. Documentation gap analysis (what's missing docs?)
4. Operational readiness check (backups, monitoring, runbooks)

**Output:** Markdown report + per-application stubs

---

## Documentation

### Start Here

**[docs/MVP-ARCHITECTURE-FOCUSED.md](docs/MVP-ARCHITECTURE-FOCUSED.md)** - The focused MVP (4 days to build)

- What to build first
- Why architects need this
- Example output (application portfolio view)
- Implementation plan

### Business & Strategy

**[docs/ROADMAP.md](docs/ROADMAP.md)** - Product evolution (4 phases, 12 weeks)

- Phase 0: MVP inventory report (Week 1-2)
- Phase 1: Trend tracking (Week 3-4)
- Phase 2: One-click fixes (Week 5-8)
- Phase 3: Doc generation (Week 9-12)
- Decision points and anti-patterns

**[docs/BUSINESS-MODEL-CANVAS.md](docs/BUSINESS-MODEL-CANVAS.md)** - Business viability

- Target: Architects (primary), Platform Engineering, FinOps
- 3 revenue models: SaaS ($120K ARR Y1), Internal platform (ROI 450%), Open source + consulting
- Service blueprint (15 min onboarding, 30-60 min weekly usage)
- Break-even: 266 Pro customers OR 20 Enterprise customers

### Technical Foundation

**[docs/AZURE-APPROACH.md](docs/AZURE-APPROACH.md)** - Azure patterns and organization

- Subscription-based organization (Azure Landing Zones)
- Tagging strategy (5 required tags: app, env, owner, cost-center, criticality)
- Resource group patterns (one capability per RG)
- Two-repo model (architecture docs vs. IaC)

**[docs/PUBLISHING-STRATEGY.md](docs/PUBLISHING-STRATEGY.md)** - How to share reports (Markdown → HTML → Data Reports)

- Phase 0: Markdown files + Git (Week 1-2)
- Phase 1: Hugo static site + Azure Static Web Apps (Week 3-4)
- Phase 2: Interactive dashboards with Chart.js (Month 2)
- Phase 3: API + dynamic queries with Cosmos DB (Month 3+)
- Enterprise integration (SharePoint, Teams, Power BI)

**[docs/DISCUSSION-INTEGRATION.md](docs/DISCUSSION-INTEGRATION.md)** - Enable discussions on inventory reports

- Phase 1: PR-based discussions in Azure DevOps (Week 3-4)
- Phase 2: Teams channel integration + notifications (Week 5-6)
- Phase 3: Embedded discussions on site via API (Week 7-8)
- Uses Azure DevOps work items as comment backend

### Archive (Future Vision)

**[archive/](archive/)** - Documents for later reference

- `ARCHITECTURE-LIFECYCLE-TOOL.md` - Full lifecycle management (build after MVP proves value)
- `MVP-comprehensive.md` - Comprehensive MVP (too ambitious, 1600 lines)
- `MVP-FOCUSED-security.md` - Old security-focused version (wrong audience)
- `VISION-platform.md` - Generic platform vision (too broad)

---

## Quick Start

### For Users (Not Built Yet)

```bash
# Install CLI (future)
pip install azure-arch-scanner

# Authenticate to Azure
az login

# Scan your environment
arch-scan --subscription "prod-customer-experience"

# View report
cat inventory.md
```

### For Contributors

1. Read **[docs/MVP-ARCHITECTURE-FOCUSED.md](docs/MVP-ARCHITECTURE-FOCUSED.md)** to understand the vision
2. Review **[docs/ROADMAP.md](docs/ROADMAP.md)** for implementation phases
3. Check **[docs/AZURE-APPROACH.md](docs/AZURE-APPROACH.md)** for Azure patterns

---

## Current Status

**Phase:** Ready to build  
**Version:** 0.1.0-planning  
**Last Updated:** November 22, 2025

**Key Decisions Made:**

- ✅ Target audience: Architects (not security teams)
- ✅ Core value: Inventory + standards compliance (not security scanning)
- ✅ Differentiation: Fills architecture gap (not competing with Defender/Security Center)
- ✅ MVP scope: 5-minute report in 4 days of dev work

**Next Steps:**

1. Build Python CLI scanner (Azure Resource Graph queries)
2. Implement grouping logic (by tags or resource groups → applications)
3. Generate markdown reports (portfolio view + per-app stubs)
4. Test against real subscription
5. Get feedback from 5 architects

---

## Core Philosophy

- **Architecture First:** Not security, not cost, not operations - this is for architects
- **Make Work Visible:** Architecture work is invisible, this makes it actionable
- **Automate Boring Chores:** Inventory, compliance checking, documentation gaps
- **Standards Compliance:** Measure what you can manage (tag compliance %, docs coverage %)
- **Progressive Enhancement:** Start simple (inventory), add complexity later (auto-fixes, doc generation)

---

## What This Is NOT

- ❌ **Not a security tool** (Azure Security Center exists)
- ❌ **Not a cost tool** (Azure Cost Management exists)
- ❌ **Not an operations tool** (Azure Monitor exists)
- ❌ **Not IaC drift detection** (Terraform Cloud exists)

**This fills the architecture gap:** application portfolio visibility, standards compliance measurement, documentation-to-reality alignment.

---

## Contributing

We welcome contributions! This is an early-stage open source project.

**How to contribute:**

1. Read the [docs/MVP-ARCHITECTURE-FOCUSED.md](docs/MVP-ARCHITECTURE-FOCUSED.md) to understand the vision
2. Check [Issues](https://github.com/YOUR_USERNAME/architecture-visibility-platform/issues) for tasks
3. Fork, create a branch, make changes, submit PR
4. Discuss in PRs or [Discussions](https://github.com/YOUR_USERNAME/architecture-visibility-platform/discussions)

**Code of Conduct:** Be respectful, constructive, and collaborative.

---

## License

MIT License - see [LICENSE](LICENSE) file.

Open source, free to use, modify, and distribute.
