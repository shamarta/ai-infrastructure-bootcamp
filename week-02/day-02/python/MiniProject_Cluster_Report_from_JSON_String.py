import json

# A JSON string, just like what a real cloud API would return
cluster_json = '''
{
  "cluster_name": "prod-cluster-1",
  "region": "eu-west-1",
  "provider": "azure",
  "created_at": "2024-01-15",
  "nodes": [
    {"id": "node-1", "status": "active", "cpu_usage": 45, "memory_gb": 16, "tags": {"env": "production", "team": "platform"}},
    {"id": "node-2", "status": "inactive", "cpu_usage": 0, "memory_gb": 8, "tags": {"env": "staging", "team": "backend"}},
    {"id": "node-3", "status": "active", "cpu_usage": 88, "memory_gb": 32, "tags": {"env": "production", "team": "platform"}},
    {"id": "node-4", "status": "active", "cpu_usage": 92, "memory_gb": 16, "tags": {"env": "production", "team": "data"}},
    {"id": "node-5", "status": "active", "cpu_usage": 33, "memory_gb": 16, "tags": {"env": "production", "team": "backend"}},
    {"id": "node-6", "status": "inactive", "cpu_usage": 0, "memory_gb": 8, "tags": {"env": "staging", "team": "data"}},
    {"id": "node-7", "status": "active", "cpu_usage": 76, "memory_gb": 32, "tags": {"env": "production", "team": "platform"}}
  ]
}
'''


def group_by_team(cluster):
    # Group node ids by their team tag
    result = {}
    for node in cluster["nodes"]:
        team = node["tags"]["team"]
        if team not in result:
            result[team] = []
        result[team].append(node["id"])
    return result


def print_cluster_report(cluster):
    active_nodes = [node for node in cluster["nodes"] if node["status"] == "active"]

    print(f"📦 Cluster: {cluster['cluster_name']} ({cluster['provider']}, {cluster['region']})")
    print(f"🖥️  Total nodes: {len(cluster['nodes'])}")
    print(f"✅ Active nodes: {len(active_nodes)}")
    print("👥 Nodes by team:")
    for team, node_ids in group_by_team(cluster).items():
        print(f"   - {team}: {node_ids}")


if __name__ == "__main__":
    # Deserialize the JSON string into a Python dictionary
    cluster = json.loads(cluster_json)
    print_cluster_report(cluster)