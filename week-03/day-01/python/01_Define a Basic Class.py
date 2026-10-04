class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage


node1 = Node("node-1", "active", 45)
print(node1.id)
print(node1.status)
print(node1.cpu_usage)