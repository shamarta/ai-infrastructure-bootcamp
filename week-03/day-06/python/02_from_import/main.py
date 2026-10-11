from models import Node, Cluster

cluster = Cluster("prod-1")
cluster.add_node(Node("node-1", "active", 45))
cluster.add_node(Node("node-2", "inactive", 0))

for node in cluster.nodes:
    print(node)