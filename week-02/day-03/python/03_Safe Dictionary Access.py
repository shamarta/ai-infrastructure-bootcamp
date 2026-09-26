def get_node_field(node, field):
    try:
        return node[field]
    except KeyError:
        return f"Field '{field}' not found"


node = {"id": "node-1", "status": "active"}

print(get_node_field(node, "status"))      # active
print(get_node_field(node, "cpu_usage"))   # Field 'cpu_usage' not found