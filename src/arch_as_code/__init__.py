"""Architecture as Code - Manage enterprise architecture programmatically.

This package provides tools to:
- Discover current state from Azure (as-is architecture)
- Define target state (to-be architecture)  
- Track changes and generate service requests

Public API:
    discover() - Discover resources from Azure
    generate_report() - Generate architecture documentation
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
