# Business Model Canvas: Architecture Visibility Platform

**Version:** 2.0  
**Date:** November 22, 2025  
**Model:** Service Blueprint + Business Model Canvas hybrid  
**Target:** Enterprise/Solution/Technical Architects

---

## Executive Summary

**Value Proposition:** "Know what you have, prove you're following standards, make architecture visible."

**Target Market:** Mid-to-large enterprises with 100+ Azure resources needing architecture governance

**Revenue Model:** Freemium SaaS, Internal Platform Team, or Open Source + Consulting

---

## 1. Customer Segments

### Primary Segments

**Segment A: Enterprise/Solution/Technical Architects (Primary Target)**

- **Size:** 5-50 per organization (mid-to-large enterprises)
- **Pain:** Spreadsheet hell for inventory, nobody follows standards, architecture work is invisible to executives, documentation always outdated
- **Budget Authority:** Medium (can approve tools <$10K/year if saves time)
- **Urgency:** High (quarterly reviews, audit prep, executive asks "what do we have?")
- **Why this segment:** Architecture gap exists (security/cost/ops have tools, architects don't)

**Segment B: Platform Engineering Teams**

- **Size:** 5-20 per organization (building internal platforms)
- **Pain:** Landing zone compliance, standards enforcement, can't measure guardrail effectiveness
- **Budget Authority:** High (part of $100K+ platform investment)
- **Urgency:** Medium (quarterly platform health checks)
- **Why this segment:** Need automated governance checks, self-service compliance

**Segment C: FinOps / Cost Optimization**

- **Size:** 1-5 per organization
- **Pain:** Can't attribute costs to applications without inventory, chargeback requires tagging
- **Budget Authority:** High (saves money, easy ROI)
- **Urgency:** Medium (monthly cost reviews)
- **Why this segment:** Need application portfolio for cost allocation

### Secondary Segments

**Segment D: Security Teams**

- **Size:** 3-10 per organization
- **Pain:** Manual security reviews take days, need operational readiness data
- **Budget Authority:** High (security tools prioritized)
- **Urgency:** Critical (compliance deadlines)
- **Why this segment:** Need inventory for risk assessment (but crowded market)

**Segment E: MSPs / Consultants**

- **Size:** Manage 10-100 client Azure tenants
- **Pain:** Need standardized auditing, client reporting
- **Budget Authority:** Medium (per-client licensing)
- **Urgency:** Low (nice-to-have, not critical)
- **Why this segment:** Recurring revenue, standardization across clients

---

## 2. Value Propositions

### Core Value Props by Segment

**For Architects:**

- ✅ Know what you have (5-minute inventory vs. 2-day spreadsheet)
- ✅ Prove standards compliance (42% → 90% tag compliance)
- ✅ Make architecture visible (portfolio view for executives)
- ✅ Automate boring chores (inventory, compliance checks)
- ✅ Detect documentation drift (docs 52 days old, deployed 37 days ago)

**For Platform Engineering:**

- ✅ Measure landing zone compliance (90% in correct subscription)
- ✅ Enforce standards at scale (85 resources missing tags - fix them)
- ✅ Self-service governance (teams check their own compliance)
- ✅ Integration with pipelines (gate deployments on compliance)

**For FinOps:**

- ✅ Application-level cost attribution (5 apps, $1750/mo)
- ✅ Tagging for chargeback (42% compliant → fix the 85 untagged)
- ✅ Cost per application (Mobile App: $650/mo, Partner Portal: $150/mo)

**For Security Teams:**

- ✅ Operational readiness checks (which apps have backups? monitoring?)
- ✅ Inventory for risk assessment (5 apps, 127 resources)
- ✅ Documentation for incident response (runbooks exist?)

### Unique Differentiators

**vs. Manual Spreadsheets (Current State):**

- 🎯 Faster (5 min scan vs. 2 days of inventory work)
- 🎯 Always current (weekly scans vs. quarterly updates)
- 🎯 Automated compliance (tag checking vs. manual review)
- 🎯 Evidence-based (discovered from Azure vs. tribal knowledge)

**vs. Azure Security Center / Defender:**

- 🎯 Architecture focus (inventory + standards, not vulnerabilities)
- 🎯 Portfolio view (5 apps with compliance %, not 1000 alerts)
- 🎯 Documentation gap detection (which apps lack docs?)
- 🎯 Standards enforcement (naming, tags, landing zones)

**vs. Terraform / IaC Drift Detection:**

- 🎯 Application-level grouping (not just resources)
- 🎯 Documentation generation (stubs for undocumented apps)
- 🎯 Multi-tool environments (works with Terraform, Bicep, Portal-deployed)
- 🎯 Business context (operational readiness, not just drift)

**vs. Terraform Drift Detection:**

- 🎯 Works without Terraform (queries Azure directly)
- 🎯 Finds problems, not just drift
- 🎯 Includes cost and documentation gaps

---

## 3. Channels (Go-To-Market)

### Phase 1: Internal/Open Source (Month 1-6)

**Channel:** GitHub + Word of Mouth

**Activities:**

1. Open source on GitHub
2. Post on Reddit (r/azureinfra, r/devops, r/enterprisearchitecture)
3. Blog post: "How we automated architecture inventory and got to 90% tag compliance"
4. Present at internal company all-hands (show architecture portfolio view)

**Cost:** $0  
**Reach:** 100-500 early adopters (architects, platform engineers)  
**Goal:** Validate product-market fit with architects

### Phase 2: Architecture Community Marketing (Month 7-12)

**Channel:** Content + Community

**Activities:**

1. Weekly blog posts (architecture governance, Azure Landing Zones patterns)
2. YouTube tutorials (5-minute architecture inventory demo)
3. Conference talks (Azure meetups, architecture conferences like SATURN, O'Reilly)
4. Free tier with generous limits (1 subscription, unlimited scans)

**Cost:** $2K/month (developer relations time)  
**Reach:** 1,000-5,000 users (architects, platform teams)  
**Goal:** Build architecture community, collect feedback

### Phase 3: Enterprise Sales (Month 13+)

**Channel:** Direct Sales + Partnerships

**Activities:**

1. Azure Marketplace listing (target: architecture teams at Fortune 500)
2. Microsoft partner program (ISV Connect)
3. Direct sales to enterprise architecture teams
4. MSP channel partnerships

**Cost:** $20K/month (1 sales, 1 SE)  
**Reach:** 50-100 enterprise customers  
**Goal:** $500K ARR

---

## 4. Customer Relationships

### Self-Service (Free/Pro Tier)

**Interaction Model:**

- Download CLI, run it yourself
- Documentation + GitHub issues for support
- Monthly "office hours" Q&A call

**Automation:**

- Automated onboarding email sequence
- Usage tips based on scan results
- Upgrade prompts when hitting limits

### Managed Service (Enterprise Tier)

**Interaction Model:**

- Slack channel for support
- Quarterly risk review calls
- Custom risk policies for their environment

**Human Touch:**

- Dedicated customer success manager
- Training workshops
- Custom integrations if needed

---

## 5. Revenue Streams

### Option A: Freemium SaaS Model

**Free Tier:**

- 1 subscription scan
- Manual scans only (no automation)
- Community support only
- Public data in reports

**Pro Tier ($99/month per subscription):**

- Unlimited scans
- Scheduled scans (weekly/daily)
- Historical trending (12 months)
- Email support

**Enterprise Tier ($999/month + $99/subscription):**

- Multi-subscription dashboard
- Custom risk policies
- Auto-fix capabilities
- SSO / RBAC
- Slack support
- SLA guarantees

**Revenue Target (Year 1):**

- 1,000 Free users → 50 Pro conversions = $60K ARR
- 5 Enterprise customers = $60K ARR
- **Total: $120K ARR**

### Option B: Internal Platform (No Revenue)

**Cost Model:**

- 1 FTE developer ($150K/year)
- Infrastructure: $5K/year
- **Total Cost: $155K/year**

**Value Delivered:**

- Fix security issues worth $500K+ risk
- Save $200K/year in cloud waste
- Reduce audit prep time by 80%
- **ROI: 450%**

### Option C: Open Source + Consulting

**Revenue Streams:**

1. **Support Subscriptions:** $5K-25K/year per customer
2. **Custom Development:** $200/hour consulting
3. **Training Workshops:** $10K per workshop
4. **GitHub Sponsors:** $1K-5K/month from community

**Revenue Target (Year 1):**

- 10 support customers = $100K
- 100 hours consulting = $20K
- 2 workshops = $20K
- **Total: $140K**

---

## 6. Key Resources

### Technology Assets

**Core Platform:**

- Python CLI application
- Azure SDK integration
- SQLite for data storage
- Markdown report generator

**IP / Differentiation:**

- Risk scoring algorithm
- Common fix templates (Terraform)
- Report formatting expertise

### Human Resources

**Phase 0-1 (MVP):**

- 1 Developer (full-time)
- 1 Azure SME (advisor, 5 hours/week)

**Phase 2-3 (Growth):**

- 2 Developers (full-time)
- 1 DevRel (content + community)
- 1 Product Manager (part-time)

**Phase 4+ (Scale):**

- 3-4 Developers
- 1 DevRel
- 1 Product Manager
- 1 Sales / Customer Success

### Infrastructure

**Development:**

- GitHub (free)
- Azure test subscription ($100/month)
- CI/CD pipelines (Azure DevOps free tier)

**Production (SaaS):**

- Azure App Service ($200/month)
- Azure SQL Database ($100/month)
- Azure Storage ($50/month)
- **Total: $350/month = $4.2K/year**

---

## 7. Key Activities

### Product Development (60% of time)

**Weekly Cadence:**

- Ship new feature every 2 weeks
- Fix bugs within 48 hours
- Review PRs within 24 hours
- Monthly planning sessions

**Priorities:**

1. Fix critical bugs (P0)
2. Complete current phase roadmap
3. High-value feature requests
4. Technical debt (15% of time)

### Customer Development (30% of time)

**Activities:**

- User interviews (2 per week)
- Monitor GitHub issues
- Community calls (monthly)
- Usage analytics review (weekly)

**Learning Goals:**

- What problems are most painful?
- What features drive adoption?
- What causes churn?
- What's the ROI story?

### Marketing (10% of time)

**Activities:**

- Weekly blog post
- Social media updates
- Conference submissions
- Partnership outreach

---

## 8. Key Partnerships

### Strategic Partnerships

**Microsoft:**

- Azure Marketplace listing
- Co-marketing opportunities
- Microsoft for Startups program
- Featured in Azure documentation

**Benefits:**

- Credibility (Microsoft endorsement)
- Distribution (Marketplace reach)
- Credits ($150K in Azure credits)

**MSPs / Consulting Firms:**

- Deloitte, Accenture, etc.
- They recommend to clients
- White-label option

**Benefits:**

- Enterprise reach
- Recurring revenue
- Proof of value at scale

### Technology Partners

**Terraform / HashiCorp:**

- Integration with Terraform Cloud
- Fix templates in Terraform registry

**ServiceNow:**

- Pre-built integration
- Change management workflow

**Benefit:** Ecosystem play, easier enterprise adoption

---

## 9. Cost Structure

### Fixed Costs (Monthly)

**Personnel:**

- 1 Developer: $12,500/month
- 0.5 Product Manager: $6,000/month
- **Total: $18,500/month**

**Infrastructure:**

- SaaS platform: $350/month
- Test environments: $100/month
- Tools & licenses: $200/month
- **Total: $650/month**

**Monthly Fixed Costs: $19,150 = $230K/year**

### Variable Costs

**Per Customer (SaaS model):**

- Azure compute: $5/month
- Storage: $2/month
- Support time: $20/month (amortized)
- **Total: $27/month per Pro customer**

**At Scale (100 customers):**

- Variable costs: $2,700/month
- Fixed costs: $19,150/month
- **Total: $21,850/month**

### Break-Even Analysis

**Pro Tier ($99/month):**

- Contribution margin: $99 - $27 = $72/customer/month
- Break-even: $19,150 / $72 = **266 customers**

**Enterprise Tier ($999/month):**

- Contribution margin: $999 - $50 = $949/customer/month
- Break-even: $19,150 / $949 = **20 customers**

**Realistic Mix (Year 1):**

- 15 Enterprise = $15K/month
- 100 Pro = $10K/month
- **Total: $25K/month = $300K ARR**
- **Profit: $300K - $230K = $70K**

---

## 10. Service Blueprint (Frontstage & Backstage)

### Frontstage (Customer-Visible)

#### Discovery & Onboarding

**Customer Actions:**

1. Find tool (GitHub, blog, word of mouth)
2. Read README / docs
3. Install CLI: `pip install azure-risk-scanner`
4. Authenticate: `az login`
5. Run first scan: `az-risk-scan --subscription prod`

**Frontstage Interactions:**

- Documentation website
- GitHub README
- Installation wizard
- CLI prompts and help text

**Duration:** 15 minutes to first value

#### Usage (Weekly Routine)

**Customer Actions:**

1. Run weekly scan
2. Review report (5 min)
3. Pick top 3 issues
4. Apply fixes (with or without auto-fix)
5. Re-scan to validate

**Frontstage Interactions:**

- CLI commands
- Markdown report output
- Fix preview/apply workflow
- Success/failure notifications

**Duration:** 30-60 min/week

#### Support & Expansion

**Customer Actions:**

1. Hit issue or confusion
2. Search docs / GitHub issues
3. Ask question (Slack/email/GitHub)
4. Get answer
5. Continue using or upgrade tier

**Frontstage Interactions:**

- Documentation search
- GitHub issues
- Email support
- Slack community
- Upgrade prompts

**Response Time:**

- Community support: 24-48 hours
- Paid support: 4 hours (business hours)
- Enterprise: 1 hour (24/7)

---

### Backstage (Behind the Scenes)

#### Infrastructure & Operations

**What Happens When Customer Runs Scan:**

1. **CLI authenticates** → Azure AD token retrieved
2. **Queries Azure Resource Graph** → Pull resource inventory
3. **Queries Security Center** → Pull security recommendations
4. **Queries Azure Advisor** → Pull cost recommendations
5. **Runs risk scoring algorithm** → Calculate severity
6. **Generates report** → Markdown with findings
7. **Stores results** (if tracking enabled) → SQLite/cloud DB
8. **Returns report** → CLI displays results

**Backstage Systems:**

- Azure SDK libraries
- Risk scoring engine
- Report templating engine
- Data persistence layer
- Usage analytics (telemetry)

**Maintenance Required:**

- Azure API monitoring (daily)
- Update risk rules (monthly)
- Update fix templates (as needed)
- Review false positives (weekly)

#### Customer Success (Enterprise)

**Backstage Activities:**

**Weekly:**

- Review customer usage metrics
- Identify customers at risk (no scans in 2 weeks)
- Send re-engagement emails

**Monthly:**

- Quarterly business review prep
- Success story documentation
- Feature request review

**Quarterly:**

- QBR with enterprise customers
- ROI calculation and presentation
- Renewal discussions (if annual)

**Tools Needed:**

- Usage analytics dashboard
- Customer health score tracking
- Email automation (Mailchimp, etc.)
- CRM (Notion, HubSpot, etc.)

#### Product Development

**Backstage Processes:**

**Weekly:**

- Triage GitHub issues
- Review feature requests (votes)
- Plan sprint (2-week cycles)
- Deploy to staging
- Deploy to production (Friday)

**Monthly:**

- Roadmap review
- User research sessions
- Performance review (metrics)
- Dependency updates

**Quarterly:**

- Major version release
- Breaking changes (if needed)
- Marketing push (blog posts, talks)

**Tools Needed:**

- GitHub (issues, PRs, projects)
- CI/CD pipeline (GitHub Actions)
- Monitoring (Azure Monitor)
- Error tracking (Sentry)

---

## Support Infrastructure

### Documentation (Backstage Investment)

**Must Have:**

- Quick start guide (5 min read)
- CLI reference (all commands)
- Risk types explained
- Fix guides (how to resolve each risk)
- FAQ (top 20 questions)

**Time Investment:** 40 hours initial, 4 hours/month maintenance

### Community Management

**Channels:**

- GitHub Issues (bug reports, features)
- GitHub Discussions (Q&A, ideas)
- Slack community (optional, later)
- Monthly community call (30 min)

**Time Investment:** 5 hours/week

### Analytics & Telemetry

**What to Track (Privacy-Respecting):**

- Scan count per user (anonymous ID)
- Average scan time
- Risk types found (aggregated)
- Fix application rate
- Error rates
- CLI version adoption

**What NOT to Track:**

- Resource names
- Customer data
- Specific findings
- Subscription IDs

**Tools:** Mixpanel or Amplitude (free tier)

---

## Growth Levers

### Viral Loops

**Mechanic:** When user runs scan, report footer includes:

```markdown
---
Generated by Azure Risk Scanner (https://github.com/yourorg/azure-risk-scanner)
Found this useful? ⭐️ Star on GitHub | Share with your team
```

**Expected k-factor:** 0.1-0.2 (10-20% share with colleague)

### Content Marketing

**Blog Post Ideas:**

1. "We found $50K in Azure waste in 5 minutes"
2. "10 Azure security mistakes that are easier to fix than you think"
3. "How we reduced our Azure risk score by 60% in one month"

**Each post → 100-500 new users**

### Conference Talks

**Target Conferences:**

- Microsoft Build
- KubeCon
- AWS re:Invent (multi-cloud angle)
- Local Azure meetups (50+ cities)

**Each talk → 50-200 new users**

### Marketplace Effect

**Azure Marketplace:**

- Listed in "Security" and "Management" categories
- Featured by Microsoft (if partnership)
- Approved vendor badge

**Expected:** 20-50 leads/month from Marketplace

---

## Risk Mitigation

### Business Risks

**Risk:** Nobody uses it  
**Mitigation:** Build MVP in 2 weeks, validate before investing more

**Risk:** False positives erode trust  
**Mitigation:** Conservative risk rules, user feedback loop

**Risk:** Microsoft builds competing feature  
**Mitigation:** Move faster, focus on UX, add value beyond scanning

**Risk:** Can't sustain free tier costs  
**Mitigation:** Usage limits, rate limiting, paid tiers introduced early

### Technical Risks

**Risk:** Azure API changes break scanner  
**Mitigation:** Automated tests, API version pinning, graceful degradation

**Risk:** Performance issues at scale  
**Mitigation:** Caching, pagination, optimize queries

**Risk:** Security vulnerability in tool  
**Mitigation:** Dependency scanning, security audits, bug bounty program

---

## Success Metrics (North Star)

### Product Metrics

**Acquisition:**

- GitHub stars: 100 (Month 1) → 1000 (Month 6)
- Weekly active users: 10 → 500
- Newsletter subscribers: 50 → 2000

**Activation:**

- % who run first scan successfully: >90%
- Time to first value: <15 minutes
- % who run 2nd scan: >60%

**Retention:**

- Weekly active users (WAU) growth
- % running weekly scans: >40%
- Churn: <5% monthly

**Revenue (if SaaS):**

- Free → Pro conversion: 5-10%
- Pro → Enterprise: 10-20%
- ARR: $120K (Year 1) → $500K (Year 2)

**Referral:**

- k-factor: 0.1-0.2
- Organic vs. paid: 80/20 split

### Impact Metrics (Customer Value)

**Efficiency:**

- Time to identify critical risks: 2 days → 5 minutes (99% reduction)
- Time to fix critical risks: 4 hours → 15 minutes (95% reduction)

**Cost Savings:**

- Average $ saved per customer: $10K-50K/year
- Average fix applied per customer: 20-50/year

**Risk Reduction:**

- Average risk score reduction: 40-60% in 3 months
- % customers with zero critical risks: 70%+

---

## Related Documents

- **[MVP-FOCUSED.md](MVP-FOCUSED.md)** - What to build first
- **[ROADMAP.md](ROADMAP.md)** - Product evolution phases
- **[README.md](README.md)** - Project overview

---

**Document Owner:** Product Strategy  
**Last Updated:** November 22, 2025  
**Status:** Business model hypothesis - validate with real customers
