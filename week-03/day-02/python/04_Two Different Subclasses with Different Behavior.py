class Node:
    def __init__(self, node_id, status):
        self.id = node_id
        self.status = status

    def resource_summary(self) -> str:
        return "No specific resources defined"


class ComputeNode(Node):
    def __init__(self, node_id, status, cpu_cores, memory_gb):
        super().__init__(node_id, status)
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb

    def resource_summary(self) -> str:
        return f"{self.cpu_cores} vCPUs, {self.memory_gb}GB RAM"


class StorageNode(Node):
    def __init__(self, node_id, status, capacity_gb):
        super().__init__(node_id, status)
        self.capacity_gb = capacity_gb

    def resource_summary(self) -> str:
        return f"{self.capacity_gb}GB storage capacity"


nodes = [
    ComputeNode("node-1", "active", cpu_cores=8, memory_gb=32),
    StorageNode("node-2", "active", capacity_gb=1000),
]

for node in nodes:
    print(f"{node.id}: {node.resource_summary()}")