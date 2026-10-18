"""Create a text health report for a small infrastructure cluster."""

DEFAULT_CPU_THRESHOLD = 80.0


def is_overloaded(cpu_percent: float, threshold: float) -> bool:
    return cpu_percent > threshold


def average_cpu_usage(nodes: list[tuple[str, float]]) -> float | None:
    if not nodes:
        return None

    return sum(cpu_percent for _, cpu_percent in nodes) / len(nodes)


def format_node_line(
    node_id: str,
    cpu_percent: float,
    threshold: float,
) -> str:
    state = "OVERLOADED" if is_overloaded(cpu_percent, threshold) else "NORMAL"
    return f"{node_id} | CPU: {cpu_percent:.1f}% | {state}"


def create_cluster_report(
    nodes: list[tuple[str, float]],
    threshold: float = DEFAULT_CPU_THRESHOLD,
) -> str:
    if not nodes:
        return "No nodes to report."

    average = average_cpu_usage(nodes)
    if average is None:
        return "No nodes to report."

    lines = [
        "Cluster health report",
        f"Nodes: {len(nodes)}",
        f"Average CPU: {average:.1f}%",
    ]

    for node_id, cpu_percent in nodes:
        lines.append(format_node_line(node_id, cpu_percent, threshold))

    return "\n".join(lines)


def main() -> None:
    cluster_nodes = [
        ("node-1", 45.0),
        ("node-2", 92.0),
        ("node-3", 66.0),
    ]
    print(create_cluster_report(cluster_nodes))


if __name__ == "__main__":
    main()
