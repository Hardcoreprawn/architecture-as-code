"""Internal data models for Architecture as Code.

These models represent internal state and can change freely.
Do not expose these directly in public APIs - use api/ contracts instead.
"""

__all__ = ["Resource", "Application"]

from .application import Application
from .resource import Resource
