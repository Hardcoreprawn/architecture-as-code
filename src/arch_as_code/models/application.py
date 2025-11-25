"""Internal application model (can change freely)."""

from dataclasses import dataclass

from .resource import Resource


@dataclass(frozen=True)
class Application:
    """Logical application grouping resources (internal representation).
    
    This is an internal model that can change freely.
    Do not expose directly in public API.
    """

    name: str
    resources: tuple[Resource, ...]  # Immutable tuple
    tags: dict[str, str]

    def calculate_compliance(self, required_tags: list[str]) -> float:
        """Calculate tag compliance percentage.
        
        Args:
            required_tags: List of tag names that should be present
            
        Returns:
            Percentage of resources with all required tags (0.0-100.0)
        """
        if not self.resources:
            return 0.0

        compliant_count = sum(
            1 for resource in self.resources if resource.has_all_tags(required_tags)
        )

        return round((compliant_count / len(self.resources)) * 100, 2)

    @property
    def resource_count(self) -> int:
        """Get number of resources in this application."""
        return len(self.resources)
