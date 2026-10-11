from infra import Cluster, Node

cluster = Cluster("prod-1")
cluster.add_node(Node("node-1", "active", 45))
cluster.add_node(Node("node-2", "active", 92))

print([str(n) for n in cluster.overloaded_nodes()])

try:
    cluster.add_node("not a node")
except TypeError as e:
    print(f"❌ {e}")