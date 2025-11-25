# Roadmap: From "Oh Shit" Report to Platform

**Version:** 1.0  
**Date:** November 22, 2025  
**Philosophy:** Ship value every 2 weeks, validate before building more

---

## Product Evolution Phases

### Phase 0: MVP - "Oh Shit" Report (Week 1-2)

**Goal:** Identify critical problems in under 5 minutes

**What Ships:**

- CLI tool: `az-risk-scan`
- Single markdown report output
- Severity ranking (Critical/High/Medium)
- Evidence with Azure CLI commands to verify
- Fix effort estimates

**Value Delivered:**

- Know what's critically broken
- Have audit-ready evidence
- Prioritized action list

**Success Metrics:**

- Runs in <5 minutes for 500 resources
- Finds 3+ critical issues (if they exist)
- Report fits on 2-3 printed pages
- 5+ people actually use it

**What We DON'T Build:**

- ❌ Automated fixes
- ❌ Historical tracking
- ❌ AI anything
- ❌ Web UI
- ❌ Integrations

---

### Phase 1: Track Progress Over Time (Week 3-4)

**Why:** "Did we actually fix anything?" needs data

**What Ships:**

- Store scan results in SQLite
- Compare this week vs. last week
- Risk score trending (up/down/same)
- Show "Fixed" and "New" issues separately

**Example Output:**

```text
📊 RISK TREND (Last 4 Weeks)

Week 11/22: 🔴 3 Critical | 🟠 8 High | 🟡 15 Medium | Score: 42
Week 11/15: 🔴 5 Critical | 🟠 9 High | 🟡 18 Medium | Score: 51
Week 11/08: 🔴 6 Critical | 🟠 11 High | 🟡 20 Medium | Score: 58
Week 11/01: 🔴 8 Critical | 🟠 12 High | 🟡 22 Medium | Score: 67

📈 IMPROVEMENT: -25 points (38% reduction in 3 weeks)

✅ FIXED THIS WEEK:
- PostgreSQL public access (Risk-001) - RESOLVED 11/19
- Storage public blobs (Risk-002) - RESOLVED 11/20

🆕 NEW THIS WEEK:
- App Service no HTTPS enforcement (Risk-015) - DETECTED 11/22
```

**Value Delivered:**

- Prove you're making progress
- Justify continued investment
- Catch new problems as they appear

**Success Metrics:**

- Show positive trend after 4 weeks
- Detect regression within 24 hours
- Management asks for weekly report

**Effort:** 3-4 days

---

### Phase 2: One-Click Fixes for Common Problems (Week 5-8)

**Why:** Fixing 80% of issues requires the same 5 changes

**What Ships:**

- Pre-built Terraform for common fixes:
  - Disable PostgreSQL public access
  - Disable storage public blob access
  - Enable CosmosDB continuous backup
  - Enable App Service HTTPS-only
  - Add missing tags
- `az-risk-scan fix <risk-id> --preview` shows what would change
- `az-risk-scan fix <risk-id> --apply` actually does it (with confirmation)
- Automatic rollback if validation fails

**Example Workflow:**

```bash
# User reviews report, sees critical issue
az-risk-scan --subscription prod

# Output shows: Risk-001: PostgreSQL public access

# Preview the fix
az-risk-scan fix risk-001 --preview
# Shows: Will disable public access, create private endpoint

# Apply it
az-risk-scan fix risk-001 --apply
# Asks: "This will modify resources. Continue? [y/N]"
# User types: y
# Output: ✅ Fixed in 2 minutes, validated, documented
```

**Safety Mechanisms:**

- Dry-run by default (--preview)
- Human confirmation required
- Validates after applying
- Rollback script generated
- Documents what was changed

**Value Delivered:**

- Fix issues in minutes instead of hours
- Reduce manual error
- Build institutional knowledge (fix patterns)

**Success Metrics:**

- 70%+ of critical issues have auto-fix available
- <5 minute end-to-end fix time
- Zero production incidents from auto-fixes
- 10+ fixes applied per week

**Effort:** 2-3 weeks (mostly testing)

---

### Phase 3: Resource Documentation Generator (Week 9-12)

**Why:** You have zero docs and need to start somewhere

**What Ships:**

- Generate basic markdown per application
- Group resources by tags or resource group
- Create placeholder architecture docs
- Auto-discover dependencies (basic)
- Generate simple C4 diagrams (ASCII art initially)

**Example Output:**

Generated file: `docs/mobile-app.md`

```markdown
---
title: "Mobile App"
generated: 2025-11-22
confidence: "medium"
needs_review: true
---

# Mobile App Architecture

> ⚠️ **Auto-generated documentation** - Requires human review and enrichment

## Discovered Resources (via tags)

**Tag filter:** `app=mobile-app`, `env=prod`

### Compute
- **Function App:** func-mobile-api-prod (Premium EP1)
  - Runtime: Node.js 20
  - Location: East US
  - Cost: ~$180/month

### Data
- **CosmosDB:** cosmos-mobile-data-prod (17GB)
  - API: NoSQL
  - Consistency: Session
  - Cost: ~$450/month

### Storage
- **Storage Account:** stmobileappprod (1.2TB)
  - Replication: LRS
  - Containers: uploads, cache, logs
  - Cost: ~$25/month

## Basic Architecture (Discovered Dependencies)

```

[Users] → [func-mobile-api-prod] → [cosmos-mobile-data-prod]
                ↓
         [stmobileappprod]

```text

## Next Steps

- [ ] Add business context and purpose
- [ ] Document actual architecture decisions
- [ ] Add operational runbooks
- [ ] Create proper C4 diagrams
- [ ] Link to project tracking
```

**Value Delivered:**

- Have *something* documented (better than nothing)
- Baseline for human enrichment
- Inventory of what actually exists

**Success Metrics:**

- Generate docs for 90%+ of resources
- Humans actually enrich 20%+ of generated docs
- Docs referenced in incident post-mortems

**Effort:** 3-4 weeks

---

## Prioritization Framework

### What Gets Built Next (Decision Tree)

```text
Is it solving a visible, urgent problem?
├─ NO → Don't build it yet
└─ YES ↓
    
    Will it save >10 hours/week for the team?
    ├─ NO → Maybe later
    └─ YES ↓
        
        Can we ship it in <2 weeks?
        ├─ NO → Break it down smaller
        └─ YES → BUILD IT
```

### Ideas Parking Lot (Not Yet)

**These are good ideas but NOT priorities:**

- 🅿️ AI-powered intelligent grouping (Phase 2 works with tags)
- 🅿️ ServiceNow integration (email is fine for now)
- 🅿️ Web UI (CLI is faster for power users)
- 🅿️ Multi-subscription management (focus on one first)
- 🅿️ Custom risk policies (use defaults first)
- 🅿️ Ephemeral test environments (overkill before auto-fixes)
- 🅿️ Change management workflow (email + manual approval works)
- 🅿️ Cost forecasting (cost reporting comes first)
- 🅿️ Compliance mapping (security fixes come first)
- 🅿️ Slack/Teams notifications (email works)

**Why park them:**

- Solving problems you don't have yet
- Adding complexity before proving value
- Optimizing before having baseline

**When to revisit:**

- After 3 months of usage
- When users explicitly ask for them
- When the pain becomes measurable

---

## Anti-Patterns to Avoid

### 🚫 Building for the Future

**Bad:** "Let's build it enterprise-ready from day 1"  
**Good:** "Let's solve today's problem and refactor when needed"

### 🚫 Feature Creep

**Bad:** "While we're at it, let's also add..."  
**Good:** "That's a great idea. Add it to the backlog for Phase N+1"

### 🚫 Perfect Architecture

**Bad:** "We need to design the whole system first"  
**Good:** "Let's build the MVP and see what breaks"

### 🚫 Premature Optimization

**Bad:** "What if we have 100,000 resources?"  
**Good:** "Let's make it work for 500, then optimize"

### 🚫 Analysis Paralysis

**Bad:** "We need 3 more weeks of research"  
**Good:** "Let's build a spike in 2 days and learn"

---

## Success Indicators by Phase

### Phase 0 (MVP)

- ✅ 10+ people run the scan
- ✅ 5+ critical issues fixed within first week
- ✅ Report referenced in weekly standup

### Phase 1 (Tracking)

- ✅ Management asks for weekly trend report
- ✅ Risk score decreases 20%+ in 4 weeks
- ✅ Team celebrates fixed issues in retrospective

### Phase 2 (Auto-Fixes)

- ✅ 50+ fixes applied in first month
- ✅ Time-to-fix drops from hours to minutes
- ✅ Other teams ask "how do we get this?"

### Phase 3 (Documentation)

- ✅ Docs used during incidents
- ✅ New team members reference generated docs
- ✅ Humans enrich 30%+ of generated content

---

## When to Pivot vs. Persevere

### Signs You Should Pivot

- Nobody uses it after 4 weeks
- Critical issues found are false positives
- Team prefers manual checks
- Takes >10 minutes to run scan
- Report is ignored in meetings

**Action:** Stop building. Interview users. Find real problem.

### Signs You Should Persevere

- Daily active users
- Issues are getting fixed
- People ask for more features
- Risk score trending down
- Other teams want access

**Action:** Keep shipping. Optimize. Add features users request.

---

## Resource Requirements

### Phase 0-1 (MVP + Tracking)

- **Dev Time:** 1 developer, 2-3 weeks
- **Infrastructure:** $0 (runs locally)
- **Dependencies:** Azure CLI, Python

### Phase 2 (Auto-Fixes)

- **Dev Time:** 1 developer, 3-4 weeks
- **Infrastructure:** $50/month (test subscription)
- **Dependencies:** Terraform, Azure permissions

### Phase 3 (Documentation)

- **Dev Time:** 1 developer, 3-4 weeks
- **Infrastructure:** $100/month (storage for docs)
- **Dependencies:** Git, Markdown processor

---

## Decision Points

### After Phase 0 (Week 2)

**Question:** Is this solving a real problem?

- **If YES:** Proceed to Phase 1
- **If NO:** Stop, interview users, reassess

### After Phase 1 (Week 4)

**Question:** Are people tracking progress?

- **If YES:** Proceed to Phase 2
- **If NO:** Improve reporting, or stop

### After Phase 2 (Week 8)

**Question:** Are people using auto-fixes?

- **If YES:** Proceed to Phase 3
- **If SOME:** Add more fix types, then Phase 3
- **If NO:** Figure out why, fix that first

### After Phase 3 (Week 12)

**Question:** Do we need more features, or is this enough?

- **If MORE:** Review parking lot, prioritize next 2-3
- **If ENOUGH:** Move to maintenance mode
- **If NEITHER:** Product might be done, archive it

---

## Exit Criteria

**When is this product "done"?**

It's done when:

1. ✅ Critical risk count stays at 0 for 4+ weeks
2. ✅ Team uses it weekly without prompting
3. ✅ New issues get fixed within 24 hours
4. ✅ Documentation coverage >80%
5. ✅ No major feature requests for 2 months

**Then what?**

- Move to maintenance mode (bug fixes only)
- Hand off to ops team for weekly scans
- Archive the backlog
- Declare victory and move on

---

## Related Documents

- **[MVP-FOCUSED.md](MVP-FOCUSED.md)** - What to build first
- **[BUSINESS-MODEL-CANVAS.md](BUSINESS-MODEL-CANVAS.md)** - How this becomes sustainable
- **[README.md](README.md)** - Project overview

---

**Document Owner:** Product-minded engineer  
**Last Updated:** November 22, 2025  
**Status:** Planning - validate with team before committing
