from .cluster import Cluster
from .models import Node


def build_demo_cluster() -> Cluster:
    cluster = Cluster("demo-cluster")
    cluster.add_node(Node("node-1", "active", 45))
    cluster.add_node(Node("node-2", "inactive", 0))
    cluster.add_node(Node("node-3", "active", 88))
    cluster.add_node(Node("node-4", "active", 92))
    return cluster


def main() -> None:
    cluster = build_demo_cluster()
    avg = cluster.average_cpu_usage()

    print(f"📦 Cluster: {cluster.name}")
    print(f"🖥️  Total nodes: {len(cluster.nodes)}")
    print(f"📊 Average active CPU: {avg:.1f}%" if avg is not None else "📊 Average active CPU: N/A")
    print(f"🚨 Overloaded nodes: {[n.id for n in cluster.overloaded_nodes()]}")