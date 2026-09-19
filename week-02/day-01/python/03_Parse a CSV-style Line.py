def parse_node_line(line ) :
    parts = line.split(",")
    result = {
        "id": parts[0],
        "status": parts[1],
        "cpu_usage": int(parts[2])
    }
    return result


line =input("Enter a node line (e.g., 'node1,active,45'): ")
result = parse_node_line(line)
print(result) # {'id': 'node1', 'status': 'active', 'cpu_usage': 45}
    
