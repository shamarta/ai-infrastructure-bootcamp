"""Inventory: a collection of nodes with reporting helpers."""

from __future__ import annotations

import json
from typing import Dict, Iterator, List, Optional

from .models import Node, node_from_dict
from .providers import CloudProvider


class Inventory:
    """Holds nodes by id and answers questions about them."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._nodes: Dict[str, Node] = {}
        self.errors: List[str] = []

    # --- container behaviour ---------------------------------------------
    def __len__(self) -> int:
        return len(self._nodes)

    def __iter__(self) -> Iterator[Node]:
        return iter(self._nodes.values())

    def __contains__(self, node_id: object) -> bool:
        return node_id in self._nodes

    def add(self, node: Node) -> None:
        if node.id in self._nodes:
            raise ValueError(f"duplicate node id: {node.id!r}")
        self._nodes[node.id] = node

    def remove(self, node_id: str) -> Node:
        try:
            return self._nodes.pop(node_id)
        except KeyError:
            raise KeyError(f"no such node: {node_id!r}") from None

    def provision_via(self, provider: CloudProvider, node_id: str, node_type: str = "compute") -> Node:
        """Ask a provider to create a node and register it in the inventory."""
        node = provider.provision(node_id, node_type)
        self.add(node)
        return node

    # --- loading ----------------------------------------------------------
    @classmethod
    def from_json(cls, name: str, json_string: str) -> "Inventory":
        """Build an inventory from a JSON array, skipping (and recording) bad records."""
        records = json.loads(json_string)  # json.JSONDecodeError is a ValueError
        if not isinstance(records, list):
            raise ValueError("JSON root must be a list of node records")

        inventory = cls(name)
        for index, record in enumerate(records):
            try:
                inventory.add(node_from_dict(record))
            except (TypeError, ValueError) as exc:
                inventory.errors.append(f"record {index}: {exc}")
        return inventory

    # --- queries ----------------------------------------------------------
    def active_nodes(self) -> List[Node]:
        return [n for n in self if n.status == "active"]

    def overloaded_nodes(self, threshold: float = 80.0) -> List[Node]:
        return [n for n in self if n.is_overloaded(threshold)]

    def average_cpu_usage(self) -> Optional[float]:
        """Average CPU of active nodes, or None when there is nothing to average."""
        active = self.active_nodes()
        if not active:
            return None
        return sum(n.cpu_usage for n in active) / len(active)

    def count_by_type(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for node in self:
            type_name = type(node).__name__
            counts[type_name] = counts.get(type_name, 0) + 1
        return counts