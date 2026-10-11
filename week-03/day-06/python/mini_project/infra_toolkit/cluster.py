from typing import List, Optional

from .models import Node


class Cluster:
    def __init__(self, name: str):
        self.name = name
        self.nodes: List[Node] = []

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)

    def average_cpu_usage(self) -> Optional[float]:
        active = [n.cpu_usage for n in self.nodes if n.status == "active"]
        return sum(active) / len(active) if active else None

    def overloaded_nodes(self) -> List[Node]:
        return [n for n in self.nodes if n.is_overloaded]