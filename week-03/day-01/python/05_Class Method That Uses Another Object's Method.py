class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

class Cluster:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def overloaded_nodes(self, threshold=80):
        return [n for n in self.nodes if n.is_overloaded(threshold)]


cluster = Cluster("prod-cluster-1", "eu-west-1")
cluster.add_node(Node("node-1", "active", 45))
cluster.add_node(Node("node-3", "active", 88))
cluster.add_node(Node("node-4", "active", 92))

for node in cluster.overloaded_nodes():
    print(node)   # از __str__ استفاده می‌کنه