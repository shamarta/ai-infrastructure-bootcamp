from .models import Node   # نقطه یعنی "از همین پکیج"


class Cluster:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def add_node(self, node):
        if not isinstance(node, Node):
            raise TypeError("Only Node objects can be added to a Cluster")
        self.nodes.append(node)

    def overloaded_nodes(self):
        return [n for n in self.nodes if n.is_overloaded()]