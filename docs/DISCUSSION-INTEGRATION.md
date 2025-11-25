# Discussion & Collaboration Integration

**Version:** 1.0  
**Date:** November 22, 2025  
**Goal:** Enable discussions on architecture inventory, leveraging existing enterprise tools

---

## Overview

Architecture inventory should be discussable - people need to comment on findings, ask questions, assign actions. We integrate with Azure DevOps and Microsoft Teams (tools enterprises already use).

---

## Phase 1: PR-Based Discussions (Week 3-4)

**Simplest approach:** Each scan creates a Pull Request in Azure DevOps

### Implementation

Scanner creates PR automatically:

```python
# scanner/publish.py
def publish_to_azure_devops(scan_results):
    date = datetime.now().strftime('%Y-%m-%d')
    branch_name = f"scan-{date}"
    
    # Create branch
    subprocess.run(['git', 'checkout', '-b', branch_name])
    
    # Generate markdown files
    generate_inventory_md(scan_results)
    generate_app_stubs(scan_results)
    
    # Commit
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'Architecture scan {date}'])
    subprocess.run(['git', 'push', 'origin', branch_name])
    
    # Create PR via Azure DevOps API
    pr = create_pull_request(
        title=f"Architecture Scan: {date}",
        description=format_pr_description(scan_results),
        source_branch=branch_name,
        target_branch='main',
        reviewers=['architects@company.com']
    )
    
    print(f"PR created: {pr['url']}")
```

PR description template:

```markdown
# Architecture Scan: 2025-11-22

## Summary
- **Total Resources:** 131 (+4 from last scan)
- **Tag Compliance:** 48% (+6% 🎉)
- **Documented Apps:** 3/5 (60%)
- **Operational Readiness:** 60%

## Changes Since Last Scan

### New Resources
- Added: `app-reporting-batch-prod` (Function App)
- Added: `stg-analytics-prod` (Storage Account)
- Added: 2 new VMs in `rg-legacy-migration`

### Compliance Improvements
- ✅ Tagged 12 resources in `mobile-app` (+15% compliance)
- ✅ Added backup to `sql-reporting-db-prod`

### Issues Found
- ⚠️ `internal-reporting` still has NO tags (0% compliance)
- ⚠️ 2 new VMs in `legacy-migration` - no owner, no docs

## Action Items
- [ ] @john.smith - Tag the `internal-reporting` resources
- [ ] @jane.doe - Document or decommission `legacy-migration` VMs
- [ ] @arch-team - Review new Function App (is this approved?)

## Full Report
See `content/inventory.md` for complete portfolio view.

---
**Next scan:** 2025-11-29  
**Contact:** architecture-team@company.com
```

### Discussion Workflow

1. **Scanner runs weekly** → Creates PR
2. **Architects get notified** → Review PR
3. **Team discusses in comments:**
   - "Why did compliance go up?"
   - "@john Can you tag those resources?"
   - "New VMs - are these approved?"
4. **Assign work items** from PR comments
5. **Merge PR** when discussed/approved

**Benefits:**

- ✅ No additional infrastructure
- ✅ Uses existing Azure DevOps workflow
- ✅ @mentions work
- ✅ Can link to work items
- ✅ History preserved in PR comments

---

## Phase 2: Teams Channel Integration (Week 5-6)

**Goal:** Link each app to Teams channel for quick discussions

### Teams Structure

```
Architecture Governance (Team)
├── Posts
│   └── #general - Announcements
├── Files
│   └── (synced from Git repo)
└── Channels
    ├── 📊 portfolio-overview
    └── Apps/
        ├── 📱 mobile-app
        ├── 🌐 customer-portal
        ├── 🌐 partner-portal
        ├── 📊 internal-reporting
        └── 💾 legacy-data-migration
```

### Hugo Site Integration

Add Teams link to each app page:

```yaml
# content/apps/mobile-app.md
---
title: "Mobile App"
teams_channel_id: "19:abc123...@thread.tacv2"
teams_channel_url: "https://teams.microsoft.com/l/channel/19:abc123..."
---
```

Hugo template:

```html
<!-- layouts/apps/single.html -->
{{ if .Params.teams_channel_url }}
<div class="teams-integration">
  <a href="{{ .Params.teams_channel_url }}" class="btn btn-teams">
    <img src="/icons/teams.svg" height="20"> 
    Discuss in Teams
  </a>
</div>
{{ end }}
```

### Auto-Post Scan Results to Teams

Scanner posts summary to Teams channel:

```python
# scanner/notify.py
import pymsteams

def notify_teams(scan_results):
    webhook_url = os.environ['TEAMS_WEBHOOK_URL']
    message = pymsteams.connectorcard(webhook_url)
    
    message.title("Architecture Scan Complete: 2025-11-22")
    message.text("Weekly architecture inventory scan has completed.")
    
    # Summary section
    summary = pymsteams.cardsection()
    summary.title("Summary")
    summary.addFact("Total Resources", "131 (+4)")
    summary.addFact("Tag Compliance", "48% (+6%)")
    summary.addFact("Documented Apps", "3/5 (60%)")
    message.addSection(summary)
    
    # Actions section
    actions = pymsteams.cardsection()
    actions.title("Action Items")
    actions.text("- Tag `internal-reporting` resources\n- Review new VMs in `legacy-migration`")
    message.addSection(actions)
    
    # Button to view report
    message.addLinkButton("View Full Report", "https://arch-inventory.azurestaticapps.net")
    
    message.send()
```

**Benefits:**

- ✅ Quick discussions (Teams is always open)
- ✅ @mention stakeholders
- ✅ Mobile-friendly
- ✅ Integrates with Outlook calendar, Planner

---

## Phase 3: Embedded Discussions on Site (Week 7-8)

**Goal:** Show discussions directly on architecture site

### Architecture

```
Hugo Site (frontend)
    ↓
Azure Static Web Apps API (backend)
    ↓
Azure DevOps REST API (work items)
```

### API Implementation

**Create discussion:**

```python
# api/discussions/__init__.py
import azure.functions as func
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == 'POST':
        return create_discussion(req)
    elif req.method == 'GET':
        return get_discussions(req)

def create_discussion(req):
    """Create Azure DevOps work item for discussion"""
    body = req.get_json()
    
    org_url = os.environ['AZURE_DEVOPS_ORG']
    pat = os.environ['AZURE_DEVOPS_PAT']
    project = os.environ['AZURE_DEVOPS_PROJECT']
    
    connection = Connection(base_url=org_url, creds=BasicAuthentication('', pat))
    wit_client = connection.clients.get_work_item_tracking_client()
    
    document = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": f"Discussion: {body['app_name']}"
        },
        {
            "op": "add",
            "path": "/fields/System.Description",
            "value": f"{body['comment']}<br><br><a href='{body['page_url']}'>View in Architecture Site</a>"
        },
        {
            "op": "add",
            "path": "/fields/System.Tags",
            "value": f"architecture-discussion; app:{body['app_name']}"
        },
        {
            "op": "add",
            "path": "/fields/System.AreaPath",
            "value": f"{project}\\Architecture\\{body['app_name']}"
        }
    ]
    
    work_item = wit_client.create_work_item(
        document=document,
        project=project,
        type='Issue'
    )
    
    return func.HttpResponse(
        json.dumps({
            "id": work_item.id,
            "url": work_item._links.additional_properties['html']['href']
        }),
        mimetype="application/json",
        status_code=201
    )

def get_discussions(req):
    """Get existing discussions for an app"""
    app_name = req.params.get('app')
    
    org_url = os.environ['AZURE_DEVOPS_ORG']
    pat = os.environ['AZURE_DEVOPS_PAT']
    project = os.environ['AZURE_DEVOPS_PROJECT']
    
    connection = Connection(base_url=org_url, creds=BasicAuthentication('', pat))
    wit_client = connection.clients.get_work_item_tracking_client()
    
    # Query work items with tag
    wiql = f"""
        SELECT [System.Id], [System.Title], [System.State], [System.AssignedTo]
        FROM WorkItems
        WHERE [System.Tags] CONTAINS 'app:{app_name}'
        AND [System.Tags] CONTAINS 'architecture-discussion'
        ORDER BY [System.CreatedDate] DESC
    """
    
    results = wit_client.query_by_wiql(
        wiql={'query': wiql},
        project=project
    )
    
    discussions = []
    for item in results.work_items[:10]:  # Latest 10
        wi = wit_client.get_work_item(item.id)
        discussions.append({
            "id": wi.id,
            "title": wi.fields['System.Title'],
            "state": wi.fields['System.State'],
            "assigned_to": wi.fields.get('System.AssignedTo', {}).get('displayName', 'Unassigned'),
            "created_date": wi.fields['System.CreatedDate'].isoformat(),
            "url": wi._links.additional_properties['html']['href']
        })
    
    return func.HttpResponse(
        json.dumps(discussions),
        mimetype="application/json"
    )
```

### Frontend Integration

Hugo template with discussions:

```html
<!-- layouts/apps/single.html -->
<div class="app-discussions">
  <h3>Discussions</h3>
  
  <button onclick="startDiscussion()" class="btn btn-primary">
    Start Discussion
  </button>
  
  <div id="discussion-list" class="mt-3">
    <p class="text-muted">Loading discussions...</p>
  </div>
</div>

<script>
const appName = "{{ .Title }}";
const pageUrl = window.location.href;

async function loadDiscussions() {
  try {
    const res = await fetch(`/api/discussions?app=${encodeURIComponent(appName)}`);
    const discussions = await res.json();
    
    const html = discussions.map(d => `
      <div class="discussion-item">
        <div class="discussion-header">
          <a href="${d.url}" target="_blank">
            <strong>${d.title}</strong>
          </a>
          <span class="badge badge-${d.state === 'Closed' ? 'success' : 'warning'}">
            ${d.state}
          </span>
        </div>
        <div class="discussion-meta">
          ${d.assigned_to} · ${new Date(d.created_date).toLocaleDateString()}
        </div>
      </div>
    `).join('');
    
    document.getElementById('discussion-list').innerHTML = 
      html || '<p class="text-muted">No discussions yet.</p>';
  } catch (err) {
    console.error(err);
    document.getElementById('discussion-list').innerHTML = 
      '<p class="text-danger">Failed to load discussions.</p>';
  }
}

async function startDiscussion() {
  const comment = prompt("What would you like to discuss about this app?");
  if (!comment) return;
  
  try {
    const res = await fetch('/api/discussions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        app_name: appName,
        page_url: pageUrl,
        comment: comment
      })
    });
    
    const result = await res.json();
    window.open(result.url, '_blank');  // Open Azure DevOps work item
    
    // Refresh discussions
    setTimeout(loadDiscussions, 1000);
  } catch (err) {
    alert('Failed to create discussion. Please try again.');
  }
}

// Load on page load
loadDiscussions();
</script>
```

**Benefits:**

- ✅ Discussions visible on site
- ✅ One-click to start discussion
- ✅ Links to Azure DevOps for full features
- ✅ Tracks in boards/backlogs

---

## Option: Real-Time Comments (Advanced)

**Phase 4 (Month 3+):** Add real-time comments with Azure SignalR

```
User types comment → Azure SignalR → All viewers see update
```

This is more like Google Docs commenting. Requires:

- Azure SignalR Service (~$50/month)
- Storage for comments (Cosmos DB)
- More complex frontend

**Recommendation:** Start with Azure DevOps work items (Phase 3), evaluate need for real-time later.

---

## Recommended Timeline

| Week | Feature | Effort | Value |
|------|---------|--------|-------|
| 3-4  | PR-based discussions | 1 day | High (uses existing workflow) |
| 5-6  | Teams channel links | 2 hours | Medium (convenience) |
| 6    | Teams webhook notifications | 4 hours | High (visibility) |
| 7-8  | Embedded discussions (API) | 2 days | High (integrated UX) |
| 12+  | Real-time comments (SignalR) | 1 week | Low (nice-to-have) |

---

## Configuration

### Environment Variables

```bash
# Azure DevOps
AZURE_DEVOPS_ORG=https://dev.azure.com/your-org
AZURE_DEVOPS_PROJECT=ArchitectureGovernance
AZURE_DEVOPS_PAT=<personal-access-token>

# Microsoft Teams
TEAMS_WEBHOOK_URL=https://outlook.office.com/webhook/...

# Static Web App
STATICWEBAPP_URL=https://arch-inventory.azurestaticapps.net
```

### Azure DevOps Setup

1. Create project: `ArchitectureGovernance`
2. Create area path: `Architecture/{AppName}`
3. Create custom work item type: `Discussion` (optional)
4. Generate PAT with permissions:
   - Work Items: Read, Write
   - Code: Read (for PR comments)

### Teams Setup

1. Create team: `Architecture Governance`
2. Create channels for each app
3. Add Incoming Webhook connector
4. Copy webhook URL to environment

---

## Security Considerations

**Authentication:**

- Static Web App uses Entra ID
- API inherits authentication
- Only authenticated users can create discussions

**Authorization:**

- Azure DevOps PAT should be service account
- Limit PAT permissions (Work Items only)
- Consider using Managed Identity instead of PAT

**Data:**

- No sensitive data in discussions (public to org)
- Link to private repos/docs in work items
- Audit log in Azure DevOps

---

## Success Metrics

**Week 4 (PR discussions):**

- ✅ 5+ architects comment on weekly PR
- ✅ 3+ action items assigned from PR comments

**Week 6 (Teams integration):**

- ✅ 10+ messages in Teams channels
- ✅ @mentions to stakeholders work

**Week 8 (Embedded discussions):**

- ✅ 5+ discussions created from site
- ✅ Average 3 comments per discussion

---

## Related Documents

- **[PUBLISHING-STRATEGY.md](PUBLISHING-STRATEGY.md)** - Site deployment
- **[MVP-ARCHITECTURE-FOCUSED.md](MVP-ARCHITECTURE-FOCUSED.md)** - Core features
- **[ROADMAP.md](ROADMAP.md)** - Timeline

---

**Document Owner:** Architecture Tool Working Group  
**Last Updated:** November 22, 2025
