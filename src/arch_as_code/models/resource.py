"""Internal resource model (can change freely)."""

from dataclasses import dataclass
from typing import TypeAlias

ResourceId: TypeAlias = str
TagName: TypeAlias = str
TagValue: TypeAlias = str


@dataclass(frozen=True)
class Resource:
    """Azure resource (internal representation).
    
    This is an internal model that can change freely.
    Do not expose directly in public API.
    """

    id: ResourceId
    name: str
    type: str
    resource_group: str
    subscription_id: str
    location: str
    tags: dict[TagName, TagValue]

    def has_tag(self, tag_name: str) -> bool:
        """Check if resource has a specific tag."""
        return tag_name in self.tags

    def has_all_tags(self, tag_names: list[str]) -> bool:
        """Check if resource has all required tags."""
        return all(self.has_tag(tag) for tag in tag_names)
