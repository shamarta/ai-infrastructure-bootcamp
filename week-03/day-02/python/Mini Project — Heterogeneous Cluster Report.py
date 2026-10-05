class Node:
    def __init__(self, node_id, status):
        self.id = node_id
        self.status = status

    def resource_summary(self):
        return "No specific resources defined"

    def __str__(self):
        return f"{self.__class__.__name__}({self.id}, {self.status})"


class ComputeNode(Node):
    def __init__(self, node_id, status, cpu_cores, memory_gb):
        super().__init__(node_id, status)
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb

    def resource_summary(self):
        return f"{self.cpu_cores} vCPUs, {self.memory_gb}GB RAM"


class StorageNode(Node):
    def __init__(self, node_id, status, capacity_gb):
        super().__init__(node_id, status)
        self.capacity_gb = capacity_gb

    def resource_summary(self):
        return f"{self.capacity_gb}GB storage capacity"


class Cluster:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def count_by_type(self):
        counts = {}
        for node in self.nodes:
            type_name = node.__class__.__name__
            counts[type_name] = counts.get(type_name, 0) + 1
        return counts

    def print_report(self):
        print(f"📦 Cluster: {self.name}")
        print(f"🖥️  Total nodes: {len(self.nodes)}")
        print("📊 Node types:", self.count_by_type())
        print("📋 Details:")
        for node in self.nodes:
            print(f"   - {node}: {node.resource_summary()}")


if __name__ == "__main__":
    cluster = Cluster("hybrid-cluster-1")
    cluster.add_node(ComputeNode("node-1", "active", cpu_cores=8, memory_gb=32))
    cluster.add_node(ComputeNode("node-2", "active", cpu_cores=16, memory_gb=64))
    cluster.add_node(StorageNode("node-3", "active", capacity_gb=1000))
    cluster.add_node(StorageNode("node-4", "inactive", capacity_gb=500))

    cluster.print_report()