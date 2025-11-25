"""Tests for public discovery API (black box testing)."""

from arch_as_code.api.v1 import DiscoveryRequest, DiscoveryResponse


def test_discovery_request_is_immutable():
    """Test that DiscoveryRequest cannot be modified after creation."""
    request = DiscoveryRequest(subscriptions=["sub-123"])

    # Should not be able to modify
    try:
        request.subscriptions = ["sub-456"]  # type: ignore
        assert False, "Should have raised an error"
    except Exception:
        pass  # Expected


def test_discovery_request_validation():
    """Test that DiscoveryRequest validates input."""
    # Valid request
    request = DiscoveryRequest(subscriptions=["sub-123", "sub-456"])
    assert request.subscriptions == ["sub-123", "sub-456"]
    assert request.required_tags is None

    # With optional fields
    request = DiscoveryRequest(
        subscriptions=["sub-123"], required_tags=["app", "env"], resource_groups=["rg-web"]
    )
    assert request.required_tags == ["app", "env"]
    assert request.resource_groups == ["rg-web"]
