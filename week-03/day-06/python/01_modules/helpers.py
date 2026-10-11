def is_overloaded(cpu_usage, threshold=80):
    return cpu_usage > threshold


def format_node(node_id, cpu_usage):
    return f"{node_id}: {cpu_usage}%"