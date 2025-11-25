# Archive: Legacy Documents

This folder contains documents that were created during the planning phase but are not part of the current focused MVP. They represent future aspirations, alternative approaches, or previous iterations.

## Why These Are Archived

The project went through several iterations before landing on the current focused approach:
1. **Started broad:** Generic platform for all architecture documentation
2. **Pivoted to Azure:** Azure-specific patterns with comprehensive features
3. **Focused on security:** "What's broken" report targeting security teams
4. **Final pivot:** Architecture inventory + standards compliance for architects

The documents below represent those earlier iterations and future vision.

---

## Documents

### `ARCHITECTURE-LIFECYCLE-TOOL.md`
**Type:** Future Vision  
**Status:** Build after MVP proves value  
**Content:** Full lifecycle management with domain-based ownership, per-application tracking, multi-audience change proposals, human-in-the-loop workflow

**Why archived:** Too comprehensive for MVP. Contains valuable ideas for Phase 3+ (after proving basic value).

### `MVP-comprehensive.md`
**Type:** Alternative MVP Approach  
**Status:** Too ambitious  
**Content:** 1600-line comprehensive MVP with Azure tenant discovery, AI grouping, multiple report types, change management features

**Why archived:** Scope creep - trying to do everything at once. Current MVP focuses on inventory + standards compliance only.

### `MVP-FOCUSED-security.md`
**Type:** Previous Iteration  
**Status:** Wrong target audience  
**Content:** Security-focused MVP targeting cloud/security teams with "Oh Shit" report of exposures, missing backups, cost waste

**Why archived:** Security is a crowded space. Architects don't need another security tool - they need inventory and standards compliance automation.

### `VISION-platform.md`
**Type:** Original Vision  
**Status:** Too generic  
**Content:** Generic enterprise architecture repository and tooling platform with git-based workflows, multiple format support, WYSIWYG editors

**Why archived:** Too broad, not focused on specific pain point. Current approach solves specific architect problem: invisible work and standards non-compliance.

### `VISION-OLD.md`
**Type:** Backup of Original Vision  
**Status:** Historical reference  
**Content:** Copy of original VISION.md before it was replaced

**Why archived:** Historical backup, no longer relevant.

---

## When to Revisit

**After MVP success (90%+ tag compliance, 5+ architect users):**
- Review `ARCHITECTURE-LIFECYCLE-TOOL.md` for Phase 3 features
- Consider comprehensive approach from `MVP-comprehensive.md` for Phase 4+
- Evaluate platform vision from `VISION-platform.md` for long-term roadmap

**If pivoting to security market:**
- Review `MVP-FOCUSED-security.md` for security-focused approach
- Note: This is a crowded space, differentiation is hard

---

## Key Lessons Learned

1. **Start focused:** Don't try to solve all architecture problems at once
2. **Know your audience:** Architects ≠ security teams (different pain points)
3. **Prove value quickly:** 4 days to MVP, not 4 months to platform
4. **Measure success:** Tag compliance % and documented apps % are measurable
5. **Fill a gap:** Security/cost/ops have tools, architects don't

---

**Last Updated:** November 22, 2025  
**Maintained by:** Architecture Tool Working Group
