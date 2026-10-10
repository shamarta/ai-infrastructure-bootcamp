from dataclasses import dataclass


@dataclass
class Node:
    id: str
    status: str
    cpu_usage: int


node = Node("node-1", "active", 45)
print(node)                                    # Node(id='node-1', status='active', cpu_usage=45)
print(node == Node("node-1", "active", 45))    # True