def has_duplicate_ips(nodes):
    # Extract all IPs into a list
    ips = [node["ip"] for node in nodes]
    # If converting to a set removes any items, there were duplicates
    return len(ips) != len(set(ips))

nodes_data = [
    {"name": "node-1", "ip": "192.168.1.10"},
    {"name": "node-2", "ip": "192.168.1.11"},
    {"name": "node-3", "ip": "192.168.1.10"},
]

print(has_duplicate_ips(nodes_data))  # Output: True (node-1 and node-3 share the same IP)