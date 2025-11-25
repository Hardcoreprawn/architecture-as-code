"""Discovery API contracts (public, stable).

These are the public API contracts for resource discovery.
Do not change without bumping API version.
"""

from pydantic import BaseModel, Field


class DiscoveryRequest(BaseModel):
    """Request to discover Azure resources (public API contract)."""

    subscriptions: list[str] = Field(..., description="List of Azure subscription IDs to scan")
    resource_groups: list[str] | None = Field(
        None, description="Optional list of resource groups to filter"
    )
    required_tags: list[str] | None = Field(
        None, description="Optional list of tags to filter by"
    )

    model_config = {"frozen": True}  # Immutable


class ApplicationSummary(BaseModel):
    """Summary of a discovered application (public API contract)."""

    name: str = Field(..., description="Application name")
    resource_count: int = Field(..., description="Number of resources in this application")
    compliance_percentage: float = Field(..., description="Tag compliance percentage (0-100)")
    cost_monthly: float | None = Field(None, description="Estimated monthly cost in USD")


class DiscoveryResponse(BaseModel):
    """Response with discovered applications (public API contract)."""

    applications: list[ApplicationSummary] = Field(..., description="Discovered applications")
    total_resources: int = Field(..., description="Total number of resources scanned")
    scan_date: str = Field(..., description="ISO 8601 timestamp of scan")

    model_config = {"frozen": True}  # Immutable
