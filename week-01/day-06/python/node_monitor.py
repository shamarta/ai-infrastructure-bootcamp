from typing import Dict, List, Set

# Sample node data (mirrors what a cloud API might return)
nodes_data: List[Dict[str, str | int]] = [
    {"id": "node-1", "ip": "192.168.1.10", "status": "active", "cpu_usage": 45},
    {"id": "node-2", "ip": "192.168.1.11", "status": "inactive", "cpu_usage": 0},
    {"id": "node-3", "ip": "192.168.1.10", "status": "active", "cpu_usage": 88},
    {"id": "node-4", "ip": "192.168.1.12", "status": "active", "cpu_usage": 92},
]


def get_unique_active_ips(nodes: List[Dict[str, str | int]]) -> Set[str]:
    # Get unique IPs of active nodes only
    return {str(node["ip"]) for node in nodes if node["status"] == "active"}


def get_high_load_nodes(nodes: List[Dict[str, str | int]], threshold: int = 80) -> List[str]:
    # Get ids of nodes whose cpu_usage is above the threshold
    return [
        str(node["id"])
        for node in nodes
        if isinstance(node["cpu_usage"], (int, float)) and node["cpu_usage"] > threshold
    ]


def get_inactive_node_ids(nodes: List[Dict[str, str | int]]) -> List[str]:
    # Get ids of nodes that are inactive
    return [str(node["id"]) for node in nodes if node["status"] == "inactive"]


def has_duplicate_ips(nodes: List[Dict[str, str | int]]) -> bool:
    # Check whether any IP appears more than once
    ips = [node["ip"] for node in nodes]
    return len(ips) != len(set(ips))


def average_cpu_usage(nodes: List[Dict[str, str | int]]) -> float | None:
    # Average cpu_usage of active nodes only; None if there's nothing to average
    if not nodes:
        return None
    active_usages = [node["cpu_usage"] for node in nodes if node["status"] == "active"]
    if not active_usages:
        return None
    return sum(active_usages) / len(active_usages)


def get_active_cpu_map(nodes: List[Dict[str, str | int]]) -> Dict[str, int]:
    # Map of {node_id: cpu_usage} for active nodes only
    return {node["id"]: node["cpu_usage"] for node in nodes if node["status"] == "active"}


def print_report(nodes: List[Dict[str, str | int]]) -> None:
    print("🌐 Unique active IPs:", get_unique_active_ips(nodes))
    print("⚠️  High load nodes (>80%):", get_high_load_nodes(nodes))
    print("💤 Inactive node ids:", get_inactive_node_ids(nodes))

    if has_duplicate_ips(nodes):
        print("🚨 Warning: duplicate IPs detected among nodes!")
    else:
        print("✅ No duplicate IPs found.")

    avg = average_cpu_usage(nodes)
    if avg is not None:
        print(f"📊 Average active CPU usage: {avg:.1f}%")
    else:
        print("📊 Average active CPU usage: no active nodes")

    print("🗺️  Active node CPU map:", get_active_cpu_map(nodes))


if __name__ == "__main__":
    print_report(nodes_data)