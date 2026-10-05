class Node:
    def __init__(self, node_id, status):
        self.id = node_id
        self.status = status

    def describe(self):
        return f"Generic node {self.id} ({self.status})"


class StorageNode(Node):
    def __init__(self, node_id, status, capacity_gb):
        super().__init__(node_id, status)
        self.capacity_gb = capacity_gb

    def describe(self):   # این متد رو کاملاً بازنویسی می‌کنیم
        return f"Storage node {self.id}: {self.capacity_gb}GB ({self.status})"


generic = Node("node-0", "active")
storage = StorageNode("node-1", "active", capacity_gb=500)

print(generic.describe())
print(storage.describe())