cluster = {
    "cluster_name": "prod-cluster", 
    "region":"eu-west-1",
    "nodes":[
        {"id": "node-1", "status": "active", "cpu_usage": 45, "tags": {"env": "production", "team": "platform"}},
        {"id": "node-2", "status": "inactive", "cpu_usage": 0, "tags": {"env": "staging", "team": "backend"}},
        {"id": "node-3", "status": "active", "cpu_usage": 88, "tags": {"env": "production", "team": "platform"}},
        {"id": "node-4", "status": "active", "cpu_usage": 92, "tags": {"env": "production", "team": "data"}},
    ]

}

print(cluster["region"])
print(len(cluster["nodes"]))
