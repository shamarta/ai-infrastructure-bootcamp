class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

    def is_overloaded(self, threshold=80):
        return self.status == "active" and self.cpu_usage > threshold

    def __str__(self):
        return f"Node({self.id}, {self.status}, {self.cpu_usage}%)"


class Cluster:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def active_node_count(self):
        return len([n for n in self.nodes if n.status == "active"])


cluster = Cluster("prod-cluster-1", "eu-west-1")
cluster.add_node(Node("node-1", "active", 45))
cluster.add_node(Node("node-2", "inactive", 0))
cluster.add_node(Node("node-3", "active", 88))

print(f"{cluster.name}: {cluster.active_node_count()} active nodes")