class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

    def is_overloaded(self, threshold=80):
        return self.status == "active" and self.cpu_usage > threshold


node1 = Node("node-1", "active", 88)
print(node1.is_overloaded())        # True
print(node1.is_overloaded(90))      # False