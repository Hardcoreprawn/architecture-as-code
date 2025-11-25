# Publishing Strategy: Markdown → HTML → Data Reports

**Version:** 1.0  
**Date:** November 22, 2025  
**Target:** Technical implementation guide

---

## Overview

Progressive enhancement from simple markdown files to interactive data reports, maintaining Git-based versioning and enterprise authentication throughout.

---

## Architecture Evolution

### Phase 0: Markdown Files (Week 1-2)

**Goal:** Prove value fast, no infrastructure

```
arch-scan → Markdown files → Git commit
```

**Tech Stack:**
- Python CLI tool
- Markdown output
- Git for versioning
- Manual sharing (copy to SharePoint, email)

**Output Structure:**
```
output/
├── 2025-11-22-scan/
│   ├── inventory.md           # Landscape view
│   ├── apps/
│   │   ├── mobile-app.md
│   │   └── customer-portal.md
│   └── data/
│       └── scan.json          # Raw data
└── latest -> 2025-11-22-scan/
```

**Pros:** Fast to build, no deployment needed  
**Cons:** Not shareable, manual process

---

### Phase 1: Static Site with Hugo (Week 3-4)

**Goal:** Shareable site, beautiful HTML, search/navigation

```
arch-scan → Markdown + Hugo → Azure Static Web Apps (with Entra ID)
```

**Tech Stack:**
- Python CLI → Markdown with front matter
- Hugo static site generator
- Azure Static Web Apps (free tier)
- Entra ID authentication
- GitHub/Azure DevOps for Git hosting

**Hugo Site Structure:**
```
arch-docs/
├── config.toml                # Hugo configuration
├── content/
│   ├── _index.md             # Homepage
│   ├── inventory.md          # Landscape view
│   └── apps/
│       ├── _index.md         # App portfolio index
│       ├── mobile-app.md
│       └── customer-portal.md
├── data/
│   └── scans/
│       └── 2025-11-22.json   # Historical scan data
├── layouts/                   # Custom templates (optional)
├── static/                    # CSS, images
└── themes/
    └── docsy/                # Or hugo-book
```

**Front Matter Example:**
```yaml
---
title: "Mobile App"
date: 2025-11-22
weight: 1
tags: ["production", "mobile", "compliant"]
compliance: 75%
cost_monthly: 650
operational_readiness: "warning"
---

# Mobile App

[← Back to Portfolio](../inventory.md)

## Summary
...
```

**Hugo Features Used:**
- **Taxonomy:** Tag apps by compliance status, environment, cost tier
- **Search:** Built-in search across all content
- **Navigation:** Auto-generated sidebar from content structure
- **Mobile-friendly:** Responsive theme
- **Fast:** Static files, no database

**Deployment:**
```yaml
# .github/workflows/deploy.yml
name: Deploy Hugo Site
on:
  push:
    branches: [main]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: peaceiris/actions-hugo@v2
      - run: hugo --minify
      - uses: azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "public"
```

**Azure Static Web Apps Configuration:**
```json
// staticwebapp.config.json
{
  "routes": [
    {
      "route": "/*",
      "allowedRoles": ["authenticated"]
    }
  ],
  "auth": {
    "identityProviders": {
      "azureActiveDirectory": {
        "registration": {
          "openIdIssuer": "https://login.microsoftonline.com/{tenant-id}/v2.0",
          "clientIdSettingName": "AZURE_CLIENT_ID",
          "clientSecretSettingName": "AZURE_CLIENT_SECRET"
        }
      }
    }
  },
  "navigationFallback": {
    "rewrite": "/404.html"
  }
}
```

**Pros:** Beautiful UI, searchable, enterprise auth, fast  
**Cons:** Still static (can't query dynamically)

---

### Phase 2: Interactive Dashboards (Month 2)

**Goal:** Add JavaScript visualizations while keeping markdown content

```
Hugo site + Chart.js + DataTables → Interactive but still static
```

**Enhancements:**
- **Compliance Trends:** Chart.js reading from `data/scans/*.json`
- **Sortable Tables:** DataTables.js for application portfolio
- **Filtering:** Filter by compliance %, cost, environment
- **Responsive Charts:** Mobile-friendly visualizations

**Example: Compliance Trend Chart**
```html
<!-- layouts/index.html -->
<div id="compliance-trend" style="height: 300px;"></div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  fetch('/data/scans/history.json')
    .then(r => r.json())
    .then(data => {
      new Chart(document.getElementById('compliance-trend'), {
        type: 'line',
        data: {
          labels: data.map(s => s.date),
          datasets: [{
            label: 'Tag Compliance %',
            data: data.map(s => s.tag_compliance),
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }]
        }
      });
    });
</script>
```

**Data Format:**
```json
// data/scans/history.json
[
  {
    "date": "2025-11-15",
    "tag_compliance": 42,
    "documented_apps": 60,
    "operational_readiness": 55,
    "total_resources": 127
  },
  {
    "date": "2025-11-22",
    "tag_compliance": 48,
    "documented_apps": 60,
    "operational_readiness": 60,
    "total_resources": 131
  }
]
```

**Pros:** Interactive, trends visible, still fast  
**Cons:** Limited to pre-generated data, can't query arbitrary time ranges

---

### Phase 3: API + Dynamic Queries (Month 3+)

**Goal:** Query historical data, compare scans, export on-demand

```
Static Site (frontend) + Azure Functions (API) + Cosmos DB (storage)
```

**Tech Stack:**
- **Frontend:** Hugo static site (as before)
- **API:** Azure Static Web Apps API (built-in Functions)
- **Storage:** Cosmos DB (JSON documents) or Azure Storage (JSON files)
- **Auth:** Entra ID (same as static content)

**API Routes:**
```
GET  /api/scans                    # List all scans
GET  /api/scans/{date}             # Get specific scan
GET  /api/scans/latest             # Get latest scan
GET  /api/apps/{name}/history      # App compliance over time
GET  /api/compliance/trend         # Compliance metrics over time
POST /api/export/{format}          # Export to PDF/Excel
```

**Example API Function:**
```python
# api/scans/__init__.py
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    client = CosmosClient.from_connection_string(os.environ['COSMOS_CONN'])
    db = client.get_database_client('arch-scans')
    container = db.get_container_client('scans')
    
    scans = list(container.query_items(
        query="SELECT * FROM c ORDER BY c.date DESC",
        enable_cross_partition_query=True
    ))
    
    return func.HttpResponse(
        json.dumps(scans),
        mimetype="application/json"
    )
```

**Frontend Integration:**
```javascript
// static/js/trends.js
async function loadComplianceTrend(appName) {
  const res = await fetch(`/api/apps/${appName}/history`);
  const data = await res.json();
  
  renderChart(data);
}
```

**Pros:** Full query capability, historical analysis, exports  
**Cons:** More complex, requires backend, costs (Cosmos DB)

---

## Recommended Timeline

| Week | Phase | Output | Sharing |
|------|-------|--------|---------|
| 1-2  | MVP: Markdown files | Local files | Manual copy to SharePoint |
| 3    | Hugo static site | Beautiful HTML | Azure Static Web Apps |
| 4    | Entra ID auth | Secure site | Share URL (enterprise SSO) |
| 5-6  | Chart.js dashboards | Interactive trends | Same site, enhanced |
| 7-8  | Search/filtering | Advanced UX | Same site, more features |
| 9+   | API + Cosmos DB | Dynamic queries | Full platform |

---

## Cost Estimate (Azure)

### Phase 1 (Hugo + Static Web Apps)
- **Azure Static Web Apps:** Free tier (100GB bandwidth/month)
- **Git hosting:** GitHub free / Azure DevOps free tier
- **Total:** $0/month

### Phase 2 (+ Interactive dashboards)
- **Same as Phase 1:** $0/month
- *(All processing client-side)*

### Phase 3 (+ API + Database)
- **Azure Static Web Apps:** Free tier (API included)
- **Cosmos DB:** Serverless tier (~$25/month for 1M reads)
- **Azure Functions:** Consumption plan (~$5/month)
- **Total:** ~$30/month

---

## Enterprise Integration

### SharePoint Integration
**Option A:** Embed in SharePoint page
```html
<iframe src="https://arch-inventory.azurestaticapps.net" 
        width="100%" height="800px"></iframe>
```

**Option B:** Link from SharePoint
- Create page in SharePoint
- Add link to Static Web Apps site
- Use same Entra ID (seamless SSO)

### Teams Integration
- Add Static Web Apps URL as Teams tab
- Appears as app within Teams
- Same Entra ID auth

### Power BI Integration (Phase 3)
- Export data to Azure Storage
- Power BI reads JSON files
- Create executive dashboards
- Embed in SharePoint/Teams

---

## Migration Path

### From Local Files to Hugo
```bash
# Existing markdown files
output/inventory.md
output/apps/mobile-app.md

# Add Hugo front matter
cat > content/inventory.md << EOF
---
title: "Architecture Inventory"
date: 2025-11-22
---
$(cat output/inventory.md)
EOF

# Initialize Hugo site
hugo new site arch-docs
cd arch-docs
git clone https://github.com/google/docsy themes/docsy
hugo serve
```

### From Hugo to Hugo+API
1. Keep all markdown content (no changes)
2. Add `api/` folder with Azure Functions
3. Add JavaScript to call API
4. Deploy: Static Web Apps auto-detects API folder

---

## Recommended Theme: Docsy

**Why Docsy:**
- Built for technical documentation
- Search built-in (Algolia or Lunr.js)
- Mobile-friendly
- Version selector (for historical scans)
- Tabbed content
- Mermaid diagram support

**Install:**
```bash
hugo new site arch-docs
cd arch-docs
git submodule add https://github.com/google/docsy themes/docsy
echo 'theme = "docsy"' >> config.toml
npm install
hugo serve
```

**Alternative: Hugo Book**
- Simpler, lighter theme
- Clean sidebar navigation
- Good for smaller sites
- Faster builds

---

## Success Metrics

**Week 3 (Hugo deployed):**
- ✅ Site loads in <2 seconds
- ✅ 5 architects can access (Entra ID)
- ✅ Search finds apps by name
- ✅ Mobile-friendly on phones/tablets

**Week 6 (Interactive dashboards):**
- ✅ Compliance trend chart loads from history
- ✅ Can filter apps by tag compliance %
- ✅ Executives view portfolio dashboard

**Week 12 (API deployed):**
- ✅ Can compare any 2 scans
- ✅ Export to PDF works
- ✅ Query "apps added in last 30 days"

---

## Related Documents

- **[MVP-ARCHITECTURE-FOCUSED.md](MVP-ARCHITECTURE-FOCUSED.md)** - What to build
- **[ROADMAP.md](ROADMAP.md)** - When to build it
- **[AZURE-APPROACH.md](AZURE-APPROACH.md)** - Azure patterns

---

**Document Owner:** Architecture Tool Working Group  
**Last Updated:** November 22, 2025
