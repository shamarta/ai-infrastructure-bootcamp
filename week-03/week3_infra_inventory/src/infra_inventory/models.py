"""Domain models: nodes and a factory that builds them from raw dictionaries."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

VALID_STATUSES = ("active", "inactive", "maintenance")


@dataclass
class Node:
    """A generic infrastructure node, validated at construction time."""

    id: str
    status: str
    cpu_usage: float

    def __post_init__(self) -> None:
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError("id must be a non-empty string")
        if not isinstance(self.status, str):
            raise TypeError("status must be a string")
        self.status = self.status.lower()
        if self.status not in VALID_STATUSES:
            raise ValueError(f"status must be one of {VALID_STATUSES}, got {self.status!r}")
        if isinstance(self.cpu_usage, bool) or not isinstance(self.cpu_usage, (int, float)):
            raise TypeError("cpu_usage must be a number")
        if not 0 <= self.cpu_usage <= 100:
            raise ValueError(f"cpu_usage must be between 0 and 100, got {self.cpu_usage}")

    def is_overloaded(self, threshold: float = 80.0) -> bool:
        """Return True if the node is active and its CPU usage exceeds the threshold."""
        return self.status == "active" and self.cpu_usage > threshold

    def resource_summary(self) -> str:
        """Describe the node's resources. Subclasses override this (polymorphism)."""
        return "no specific resources"


@dataclass
class ComputeNode(Node):
    """A node whose main purpose is running workloads."""

    cpu_cores: int = 2
    memory_gb: int = 8

    def __post_init__(self) -> None:
        super().__post_init__()
        for name, value in (("cpu_cores", self.cpu_cores), ("memory_gb", self.memory_gb)):
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"{name} must be a positive integer, got {value!r}")

    def resource_summary(self) -> str:
        return f"{self.cpu_cores} vCPUs, {self.memory_gb}GB RAM"


@dataclass
class StorageNode(Node):
    """A node whose main purpose is storing data."""

    capacity_gb: int = 100

    def __post_init__(self) -> None:
        super().__post_init__()
        if isinstance(self.capacity_gb, bool) or not isinstance(self.capacity_gb, int) or self.capacity_gb <= 0:
            raise ValueError(f"capacity_gb must be a positive integer, got {self.capacity_gb!r}")

    def resource_summary(self) -> str:
        return f"{self.capacity_gb}GB storage"


NODE_TYPES = {
    "generic": Node,
    "compute": ComputeNode,
    "storage": StorageNode,
}


def node_from_dict(data: Dict[str, Any]) -> Node:
    """Build the right Node subclass from a raw dictionary (e.g. one API record).

    The optional "type" key selects the class; it defaults to "generic".
    Raises ValueError for an unknown type, and TypeError for missing/unexpected fields.
    """
    fields = dict(data)  # never mutate the caller's data
    node_type = fields.pop("type", "generic")
    if isinstance(node_type, str):
        node_type = node_type.lower()
    try:
        node_class = NODE_TYPES[node_type]
    except KeyError:
        raise ValueError(f"unknown node type: {node_type!r}") from None
    return node_class(**fields)