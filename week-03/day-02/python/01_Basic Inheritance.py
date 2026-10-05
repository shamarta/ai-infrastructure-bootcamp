class Node:
    def __init__(self, node_id, status):
        self.id = node_id
        self.status = status

    def __str__(self):
        return f"{self.__class__.__name__}({self.id}, {self.status})"


class ComputeNode(Node):
    pass


node = ComputeNode("node-1", "active")
print(node)                  
print(isinstance(node, Node))  