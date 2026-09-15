from typing import Dict, List, Optional

nodes_data: List[Dict[str, str | int]] = [
    {"id": "node-1", "ip": "192.168.1.10", "status": "active", "cpu_usage": 45},
    {"id": "node-2", "ip": "192.168.1.11", "status": "inactive", "cpu_usage": 0},
    {"id": "node-3", "ip": "192.168.1.10", "status": "active", "cpu_usage": 88},
    {"id": "node-4", "ip": "192.168.1.12", "status": "active", "cpu_usage": 92},
]


def get_unique_active_ips(nodes):
    # Get unique IPs of active nodes only
    return {str(node["ip"]) for node in nodes if node["status"] == "active"}


def average_cpu_usage(nodes) -> Optional[float]:
    # Average cpu_usage of active nodes only; None if there's nothing to average
    active_usages = [node["cpu_usage"] for node in nodes if node["status"] == "active"]
    if not active_usages:
        return None
    return sum(active_usages) / len(active_usages)


def get_node_summary(nodes) -> Dict[str, object]:
    # Combine smaller functions into one summary dictionary
    active_nodes = [node for node in nodes if node["status"] == "active"]
    inactive_nodes = [node for node in nodes if node["status"] == "inactive"]

    return {
        "total_nodes": len(nodes),
        "active_count": len(active_nodes),
        "inactive_count": len(inactive_nodes),
        "unique_ips": len(get_unique_active_ips(nodes)),
        "avg_active_cpu": average_cpu_usage(nodes),
    }


print(get_node_summary(nodes_data))
# Output:
# {'total_nodes': 4, 'active_count': 3, 'inactive_count': 1,
#  'unique_ips': 2, 'avg_active_cpu': 75.0}