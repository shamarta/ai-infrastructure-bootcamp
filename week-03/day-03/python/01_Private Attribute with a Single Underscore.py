class Node:
    def __init__(self, node_id, cpu_usage):
        self.id = node_id
        self._cpu_usage = cpu_usage   # convention: "internal use only"

    def get_cpu_usage(self):
        return self._cpu_usage


node = Node("node-1", 45)
print(node.get_cpu_usage())   
print(node._cpu_usage)       