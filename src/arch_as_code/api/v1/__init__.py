"""Public API contracts for Architecture as Code v1.

These contracts define the stable public API. Internal models may change,
but these contracts should remain backwards compatible.
"""

__all__ = ["DiscoveryRequest", "DiscoveryResponse"]

from .discovery import DiscoveryRequest, DiscoveryResponse
