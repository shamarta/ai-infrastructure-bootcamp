"""
node_monitor.py

A small toolkit for parsing and summarizing cloud node status data
(the kind of data typically returned by a cloud provider's API).
"""

from typing import Dict, List, Optional, Set, Union

Node = Dict[str, Union[str, int]]


def get_unique_active_ips(nodes: List[Node]) -> Set[str]:
    """Return the set of unique IP addresses belonging to active nodes."""
    return {str(node["ip"]) for node in nodes if node["status"] == "active"}


def get_high_load_nodes(nodes: List[Node], threshold: int = 80) -> List[str]:
    """Return ids of nodes whose cpu_usage exceeds the given threshold."""
    return [
        str(node["id"])
        for node in nodes
        if isinstance(node["cpu_usage"], (int, float)) and node["cpu_usage"] > threshold
    ]


def get_inactive_node_ids(nodes: List[Node]) -> List[str]:
    """Return ids of nodes whose status is 'inactive'."""
    return [str(node["id"]) for node in nodes if node["status"] == "inactive"]


def has_duplicate_ips(nodes: List[Node]) -> bool:
    """Return True if any IP address appears more than once among the nodes."""
    ips = [node["ip"] for node in nodes]
    return len(ips) != len(set(ips))


def average_cpu_usage(nodes: List[Node]) -> Optional[float]:
    """
    Return the average cpu_usage of active nodes.

    Returns None (not 0) when there are no active nodes, to distinguish
    "no data" from "zero average load".
    """
    active_usages = [node["cpu_usage"] for node in nodes if node["status"] == "active"]
    if not active_usages:
        return None
    return sum(active_usages) / len(active_usages)


def get_active_cpu_map(nodes: List[Node]) -> Dict[str, int]:
    """Return a mapping of {node_id: cpu_usage} for active nodes only."""
    return {str(node["id"]): node["cpu_usage"] for node in nodes if node["status"] == "active"}


def get_node_summary(nodes: List[Node]) -> Dict[str, object]:
    """Return an aggregated summary of the node list."""
    active_nodes = [n for n in nodes if n["status"] == "active"]
    inactive_nodes = [n for n in nodes if n["status"] == "inactive"]

    return {
        "total_nodes": len(nodes),
        "active_count": len(active_nodes),
        "inactive_count": len(inactive_nodes),
        "unique_ips": len(get_unique_active_ips(nodes)),
        "avg_active_cpu": average_cpu_usage(nodes),
    }


def print_report(nodes: List[Node]) -> None:
    """Print a human-readable status report for the given nodes."""
    print("🌐 Unique active IPs:", get_unique_active_ips(nodes))
    print("⚠️  High load nodes (>80%):", get_high_load_nodes(nodes))
    print("💤 Inactive node ids:", get_inactive_node_ids(nodes))
    print("🚨 Duplicate IPs detected!" if has_duplicate_ips(nodes) else "✅ No duplicate IPs found.")

    avg = average_cpu_usage(nodes)
    print(f"📊 Average active CPU usage: {avg:.1f}%" if avg is not None else "📊 Average active CPU usage: no active nodes")

    print("🗺️  Active node CPU map:", get_active_cpu_map(nodes))


if __name__ == "__main__":
    sample_nodes: List[Node] = [
        {"id": "node-1", "ip": "192.168.1.10", "status": "active", "cpu_usage": 45},
        {"id": "node-2", "ip": "192.168.1.11", "status": "inactive", "cpu_usage": 0},
        {"id": "node-3", "ip": "192.168.1.10", "status": "active", "cpu_usage": 88},
        {"id": "node-4", "ip": "192.168.1.12", "status": "active", "cpu_usage": 92},
    ]
    print_report(sample_nodes)