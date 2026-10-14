"""Cloud provider interface and two concrete implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import Node, node_from_dict


class CloudProvider(ABC):
    """Contract every cloud provider must fulfil."""

    name: str

    @abstractmethod
    def provision(self, node_id: str, node_type: str = "compute") -> Node:
        """Create a new node and return it."""

    @abstractmethod
    def decommission(self, node: Node) -> str:
        """Shut a node down and return a human-readable message."""


class AzureProvider(CloudProvider):
    name = "azure"

    def provision(self, node_id: str, node_type: str = "compute") -> Node:
        return node_from_dict(
            {"id": node_id, "type": node_type, "status": "active", "cpu_usage": 0}
        )

    def decommission(self, node: Node) -> str:
        node.status = "inactive"
        return f"Azure: deallocated VM '{node.id}'"


class AWSProvider(CloudProvider):
    name = "aws"

    def provision(self, node_id: str, node_type: str = "compute") -> Node:
        return node_from_dict(
            {"id": node_id, "type": node_type, "status": "active", "cpu_usage": 0}
        )

    def decommission(self, node: Node) -> str:
        node.status = "inactive"
        return f"AWS: terminated instance '{node.id}'"