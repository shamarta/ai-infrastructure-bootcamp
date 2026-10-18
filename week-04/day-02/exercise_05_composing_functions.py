"""Exercise 5: compose small functions to create a cluster report."""


def format_node(node_id: str, cpu_percent: float) -> str:
    return f"{node_id} | CPU: {cpu_percent:.1f}%"


def is_overloaded(cpu_percent: float, threshold: float = 80.0) -> bool:
    return cpu_percent > threshold


def create_report(
    nodes: list[tuple[str, float]],
    threshold: float = 80.0,
) -> str:
    lines = []

    for node_id, cpu_percent in nodes:
        node_line = format_node(node_id, cpu_percent)
        if is_overloaded(cpu_percent, threshold):
            node_line += " | OVERLOADED"
        lines.append(node_line)

    return "\n".join(lines) if lines else "No nodes to report."


if __name__ == "__main__":
    cluster = [("node-1", 42.0), ("node-2", 88.5)]
    print(create_report(cluster))
