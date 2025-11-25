# Coding Standards

**Version:** 1.0  
**Date:** November 25, 2025  
**Purpose:** Standards for AI agents and human contributors

---

## Core Principles

### 1. Functional Code Style

- **Prefer pure functions:** No side effects when possible
- **Immutable data:** Use dataclasses with `frozen=True`, avoid mutating inputs
- **Composition over inheritance:** Small, composable functions
- **Explicit is better than implicit:** Clear function signatures, no magic

### 2. Black Box Testing

- **Test behavior, not implementation:** Test public interfaces only
- **No access to private methods/attributes:** If you need to test it, make it public or refactor
- **Integration tests over unit tests:** Test real workflows
- **Smoke tests when things fail:** When bugs occur, add a smoke test to prevent regression

### 3. API Contracts

- **Separate public API from internal models:**
  - `/api/` - Public API contracts (what users see)
  - `/models/` - Internal data models (implementation details)
- **Version APIs explicitly:** `v1/`, `v2/` when breaking changes needed
- **Use Pydantic for validation:** Type-safe contracts with automatic validation
- **Document with docstrings:** What it does, not how it does it

### 4. File Size Management

- **Max 300 lines per file:** Split larger files into modules
- **Single responsibility:** One file, one clear purpose
- **Use `__init__.py` to expose clean APIs:** Hide complexity behind simple imports

---

## Python Standards

### Code Style

```python
# Use Black formatter (line length: 100)
# Use Ruff for linting
# Use mypy for type checking

# Good: Functional, type-hinted
def calculate_compliance(resources: list[Resource]) -> ComplianceReport:
    """Calculate tag compliance percentage for resources.
    
    Args:
        resources: List of Azure resources to analyze
        
    Returns:
        ComplianceReport with compliance percentage and details
    """
    total = len(resources)
    compliant = sum(1 for r in resources if has_required_tags(r))
    return ComplianceReport(
        total=total,
        compliant=compliant,
        percentage=round(compliant / total * 100, 2) if total > 0 else 0.0
    )

# Bad: Mutation, unclear types
def calculate_compliance(resources):
    resources.sort()  # Mutates input!
    count = 0
    for r in resources:
        if r.tags:  # What tags? Required tags?
            count += 1
    return count / len(resources) * 100  # Returns what type?
```

### Type Hints

```python
from typing import TypeAlias
from pydantic import BaseModel

# Define type aliases for clarity
ResourceId: TypeAlias = str
TagName: TypeAlias = str

# Use Pydantic for data validation
class Resource(BaseModel):
    """Azure resource (internal model)."""
    id: ResourceId
    name: str
    type: str
    tags: dict[TagName, str]
    
# API contracts use Pydantic too
class InventoryResponse(BaseModel):
    """API response for inventory query (public contract)."""
    resources: list[Resource]
    total_count: int
    compliance_percentage: float
```

### Error Handling

```python
# Good: Specific exceptions, helpful messages
class AuthenticationError(Exception):
    """Failed to authenticate to Azure."""
    pass

def get_subscriptions() -> list[Subscription]:
    try:
        # Azure SDK call
        subs = client.subscriptions.list()
        return list(subs)
    except ClientAuthenticationError as e:
        raise AuthenticationError(
            "Failed to authenticate. Run 'az login' first."
        ) from e

# Bad: Swallowing exceptions, vague errors
def get_subscriptions():
    try:
        return list(client.subscriptions.list())
    except:
        return []  # What went wrong? How to fix?
```

---

## Testing Standards

### Black Box Testing

```python
# Good: Test public API only
def test_compliance_calculation():
    """Test that compliance percentage is calculated correctly."""
    # Arrange
    resources = [
        create_resource(tags={"app": "web", "env": "prod"}),
        create_resource(tags={"app": "api"}),  # Missing env
        create_resource(tags={}),  # No tags
    ]
    
    # Act
    report = calculate_compliance(resources, required_tags=["app", "env"])
    
    # Assert
    assert report.percentage == 33.33
    assert report.compliant == 1
    assert report.total == 3

# Bad: Testing implementation details
def test_compliance_calculation():
    calc = ComplianceCalculator()
    calc._internal_counter = 0  # Accessing private attribute!
    calc._process_resources()  # Testing private method!
    assert calc._internal_counter == 3  # Brittle, breaks on refactor
```

### Smoke Tests

```python
# When a bug occurs, add a smoke test
def test_empty_resources_doesnt_crash():
    """Smoke test: Don't crash on empty resource list (issue #42)."""
    report = calculate_compliance([], required_tags=["app"])
    assert report.percentage == 0.0
    assert report.total == 0

def test_resources_without_tags_field():
    """Smoke test: Handle resources missing tags field (issue #58)."""
    resource = {"id": "123", "name": "test"}  # No 'tags' key
    result = has_required_tags(resource, ["app"])
    assert result is False  # Should not raise KeyError
```

### Test File Structure

```text
tests/
├── api/                    # Test public APIs
│   ├── test_inventory.py
│   └── test_compliance.py
├── integration/            # Test real workflows
│   ├── test_azure_discovery.py
│   └── test_report_generation.py
└── smoke/                  # Regression tests
    ├── test_edge_cases.py
    └── test_bug_fixes.py
```

---

## File Organization

### Max 300 Lines Per File

```text
src/arch_as_code/
├── __init__.py           # Clean public API
├── cli.py                # CLI entry point (<300 lines)
├── discovery/
│   ├── __init__.py       # Export: discover_resources()
│   ├── azure_client.py   # Azure SDK wrapper (<300)
│   ├── query_builder.py  # Resource Graph queries (<300)
│   └── grouping.py       # Group resources by app (<300)
├── compliance/
│   ├── __init__.py       # Export: check_compliance()
│   ├── tags.py           # Tag compliance (<300)
│   └── naming.py         # Naming conventions (<300)
└── reporting/
    ├── __init__.py       # Export: generate_report()
    ├── markdown.py       # Markdown generation (<300)
    └── json.py           # JSON serialization (<300)
```

### Clean Module APIs

```python
# src/arch_as_code/discovery/__init__.py
"""Azure resource discovery module.

Public API:
    discover_resources() - Main entry point
    DiscoveryConfig - Configuration dataclass
    DiscoveryResult - Result dataclass
"""

from .azure_client import AzureClient
from .query_builder import build_query
from .grouping import group_by_application

# Public API
__all__ = [
    "discover_resources",
    "DiscoveryConfig", 
    "DiscoveryResult",
]

def discover_resources(config: DiscoveryConfig) -> DiscoveryResult:
    """Discover Azure resources and group by application.
    
    Args:
        config: Discovery configuration (subscriptions, tags, etc.)
        
    Returns:
        DiscoveryResult with grouped resources
    """
    client = AzureClient.from_cli()  # Internal detail
    resources = client.query(build_query(config))  # Internal detail
    return group_by_application(resources, config.grouping)  # Internal detail
```

---

## API Contracts vs Internal Models

### Separation Pattern

```text
src/arch_as_code/
├── api/                    # PUBLIC contracts (stable, versioned)
│   ├── v1/
│   │   ├── inventory.py    # InventoryRequest, InventoryResponse
│   │   └── compliance.py   # ComplianceRequest, ComplianceResponse
│   └── __init__.py
└── models/                 # INTERNAL models (can change freely)
    ├── resource.py         # Resource, ResourceGroup (internal repr)
    ├── application.py      # Application (internal grouping)
    └── scan.py            # ScanResult (internal state)
```

### Example: API Contract

```python
# api/v1/inventory.py (PUBLIC - stable)
from pydantic import BaseModel

class InventoryRequest(BaseModel):
    """Request to discover resources (public API contract)."""
    subscriptions: list[str]
    include_tags: list[str] | None = None
    
class InventoryResponse(BaseModel):
    """Response with discovered resources (public API contract)."""
    applications: list[dict]  # Simplified for API
    total_resources: int
    scan_date: str
```

### Example: Internal Model

```python
# models/application.py (INTERNAL - can change)
from dataclasses import dataclass

@dataclass(frozen=True)
class Application:
    """Internal representation of a logical application."""
    name: str
    resources: tuple[Resource, ...]  # Frozen for immutability
    tags: dict[str, str]
    cost_monthly: float | None
    compliance_score: float
    
    # Complex internal logic here
    def calculate_health_score(self) -> float:
        """Internal method, not exposed in API."""
        ...
```

### Mapping Between API and Internal

```python
# services/inventory.py
from api.v1.inventory import InventoryRequest, InventoryResponse
from models.application import Application

def handle_inventory_request(req: InventoryRequest) -> InventoryResponse:
    """Map public API to internal models and back."""
    # Use internal models for business logic
    apps: list[Application] = discover_applications(req.subscriptions)
    
    # Map internal model to API response
    return InventoryResponse(
        applications=[
            {
                "name": app.name,
                "resource_count": len(app.resources),
                "compliance": app.compliance_score,
            }
            for app in apps
        ],
        total_resources=sum(len(app.resources) for app in apps),
        scan_date=datetime.now().isoformat(),
    )
```

---

## Tool Configuration

### pyproject.toml

```toml
[project]
name = "architecture-as-code"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "azure-identity>=1.15.0",
    "azure-mgmt-resource>=23.0.0",
    "azure-mgmt-resourcegraph>=8.0.0",
    "pydantic>=2.5.0",
    "typer>=0.9.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.12.0",
    "ruff>=0.1.8",
    "mypy>=1.7.1",
]

[tool.black]
line-length = 100
target-version = ["py311"]

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "UP", "PL"]
ignore = ["E501"]  # Black handles line length

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
addopts = "--cov=src --cov-report=html --cov-report=term"
```

### Pre-commit Hook (Optional)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.8
    hooks:
      - id: ruff
        args: [--fix]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
```

---

## Documentation Standards

### Function Docstrings

```python
def discover_resources(
    subscriptions: list[str],
    required_tags: list[str] | None = None
) -> DiscoveryResult:
    """Discover Azure resources across subscriptions.
    
    Queries Azure Resource Graph to find all resources in the specified
    subscriptions, then filters and groups them by application.
    
    Args:
        subscriptions: List of subscription IDs to scan
        required_tags: Optional list of tags to filter by
        
    Returns:
        DiscoveryResult containing grouped applications and metadata
        
    Raises:
        AuthenticationError: If Azure authentication fails
        SubscriptionNotFoundError: If subscription doesn't exist
        
    Example:
        >>> result = discover_resources(["sub-123"], required_tags=["app"])
        >>> print(result.applications[0].name)
        'mobile-app'
    """
```

### Module Docstrings

```python
"""Azure resource discovery module.

This module provides functionality to discover and group Azure resources
using Azure Resource Graph queries. It handles authentication, query
building, and grouping logic.

Public API:
    discover_resources() - Main entry point
    DiscoveryConfig - Configuration
    DiscoveryResult - Result wrapper
    
Internal modules:
    azure_client - Azure SDK wrapper (not exposed)
    query_builder - Query generation (not exposed)
    grouping - Resource grouping (not exposed)
"""
```

---

## AI Agent Instructions

**When contributing code, AI agents MUST:**

1. ✅ Write pure functions with no side effects when possible
2. ✅ Use type hints for all function signatures
3. ✅ Keep files under 300 lines (split if larger)
4. ✅ Separate API contracts (`api/`) from internal models (`models/`)
5. ✅ Test public APIs only (black box testing)
6. ✅ Add smoke tests when bugs are found
7. ✅ Use Pydantic for data validation
8. ✅ Format with Black (line length: 100)
9. ✅ Lint with Ruff
10. ✅ Type check with mypy

**When reviewing code, check:**

- [ ] File is under 300 lines?
- [ ] All functions have type hints?
- [ ] API contracts are in `api/`, internal models in `models/`?
- [ ] Tests only use public APIs?
- [ ] Docstrings explain what, not how?
- [ ] No mutation of input parameters?

---

## Related Documents

- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - How to contribute
- **[docs/MVP-ARCHITECTURE-FOCUSED.md](MVP-ARCHITECTURE-FOCUSED.md)** - What we're building

---

**Document Owner:** Architecture Tool Working Group  
**Last Updated:** November 25, 2025
