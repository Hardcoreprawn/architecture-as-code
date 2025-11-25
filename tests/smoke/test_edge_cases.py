"""Smoke tests for edge cases and bug fixes.

When bugs are discovered, add a smoke test here to prevent regression.
"""

from arch_as_code.models import Application, Resource

# Compliance constants
ZERO_COMPLIANCE = 0.0
FULL_COMPLIANCE = 100.0


def test_empty_application_compliance():
    """Smoke test: Empty application should return 0% compliance, not crash."""
    app = Application(name="test", resources=(), tags={})

    compliance = app.calculate_compliance(required_tags=["app", "env"])

    assert compliance == ZERO_COMPLIANCE


def test_resource_without_tags():
    """Smoke test: Resource with no tags should handle missing tags gracefully."""
    resource = Resource(
        id="/subscriptions/123/resourceGroups/test/providers/Microsoft.Compute/virtualMachines/vm1",
        name="vm1",
        type="Microsoft.Compute/virtualMachines",
        resource_group="test",
        subscription_id="123",
        location="eastus",
        tags={},  # No tags
    )

    assert not resource.has_tag("app")
    assert not resource.has_all_tags(["app", "env"])


def test_application_with_single_resource():
    """Smoke test: Application with one resource should calculate compliance correctly."""
    resource = Resource(
        id="/subscriptions/123/resourceGroups/test/providers/Microsoft.Compute/virtualMachines/vm1",
        name="vm1",
        type="Microsoft.Compute/virtualMachines",
        resource_group="test",
        subscription_id="123",
        location="eastus",
        tags={"app": "web", "env": "prod"},
    )

    app = Application(name="web", resources=(resource,), tags={"app": "web"})

    compliance = app.calculate_compliance(required_tags=["app", "env"])

    assert compliance == FULL_COMPLIANCE
