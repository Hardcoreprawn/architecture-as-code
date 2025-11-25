"""Azure resource discovery module.

This module discovers resources from Azure and groups them by application.
"""

__all__ = ["discover_resources"]


def discover_resources(subscription_id: str) -> list:
    """Discover Azure resources in a subscription.
    
    Args:
        subscription_id: Azure subscription ID
        
    Returns:
        List of discovered resources (placeholder)
        
    Raises:
        NotImplementedError: Not yet implemented - see issue #1
    """
    raise NotImplementedError("Discovery not yet implemented - see issue #1")
