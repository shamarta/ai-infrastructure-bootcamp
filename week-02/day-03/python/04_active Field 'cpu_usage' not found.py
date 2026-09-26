def parse_node_line_safe(line):
    try:
        parts = line.split(",")
        result = {
            "id": parts[0],
            "status": parts[1],
            "cpu_usage": int(parts[2])
        }
        return result
    except (IndexError, ValueError):
        return None


print(parse_node_line_safe("node-1,active,45"))   # {'id': 'node-1', 'status': 'active', 'cpu_usage': 45}
print(parse_node_line_safe("node-2,active"))        # None ( IndexError)
print(parse_node_line_safe("node-3,active,high"))   # None (cpu_usage , ValueError)