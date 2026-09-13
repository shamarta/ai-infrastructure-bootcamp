nodes_data = [
    {"id": "node-1", "status": "active", "cpu_usage": 45},
    {"id": "node-2", "status": "offline", "cpu_usage": 10},
    {"id": "node-3", "status": "active", "cpu_usage": 88},
    {"id": "node-4", "status": "active", "cpu_usage": 92},
    {"id": "node-5", "status": "maintenance", "cpu_usage": 30},
]


def get_active_cpu_map(nodes):
    # Build a dictionary of {node_id: cpu_usage} for active nodes only
    return {node["id"]: node["cpu_usage"] for node in nodes if node["status"] == "active"}


print(get_active_cpu_map(nodes_data))
# Output: {'node-1': 45, 'node-3': 88, 'node-4': 92}