nodes_data = [
    {"id": "node-1", "ip": "192.168.1.10", "status": "active", "cpu_usage": 45},
    {"id": "node-2", "ip": "192.168.1.11", "status": "inactive", "cpu_usage": 0},
    {"id": "node-3", "ip": "192.168.1.10", "status": "active", "cpu_usage": 88},
    {"id": "node-4", "ip": "192.168.1.12", "status": "active", "cpu_usage": 92},
]

def get_inactive_node_ids(nodes):
    # Return the id of every node whose status is "inactive"
    return [node["id"] for node in nodes if node["status"] == "inactive"]

print(get_inactive_node_ids(nodes_data))  # Output: ['node-2']