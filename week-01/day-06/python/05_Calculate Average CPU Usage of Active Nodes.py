def average_cpu_usage(nodes):
    if not nodes:
        return None
    active_usages = [node["cpu_usage"] for node in nodes if node["status"] == "active"]
    if not active_usages:
        return None
    return sum(active_usages) / len(active_usages)

node_data = [
    {"status": "active", "cpu_usage": 50},
    {"status": "inactive", "cpu_usage": 90},
    {"status": "active", "cpu_usage": 70},
]

print(average_cpu_usage(node_data))
print(average_cpu_usage([]))  # Test with an empty list