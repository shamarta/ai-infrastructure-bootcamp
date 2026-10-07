class Node:
    def __init__(self, node_id, cpu_usage):
        self.id = node_id
        self._cpu_usage = cpu_usage

    @property
    def cpu_usage(self):
        return self._cpu_usage


node = Node("node-1", 45)
print(node.cpu_usage)        # 45

try:
    node.cpu_usage = 90
except AttributeError as e:
    print(f"❌ Expected error: {e}")