"""Functional-style helpers for analyzing infrastructure node metrics."""

DEFAULT_CPU_THRESHOLD = 80.0
Node = tuple[str, float]


def format_cpu_usages(usages: list[float]) -> list[str]:
    """Format CPU values as percentages."""
    return list(map(lambda usage: f"{usage:.1f}%", usages))


def select_overloaded_nodes(
    nodes: list[Node],
    threshold: float = DEFAULT_CPU_THRESHOLD,
) -> list[Node]:
    """Return nodes whose CPU usage is above the threshold."""
    return list(filter(lambda node: node[1] > threshold, nodes))


def sort_nodes_by_cpu(
    nodes: list[Node],
    descending: bool = True,
) -> list[Node]:
    """Return nodes sorted by CPU usage."""
    return sorted(nodes, key=lambda node: node[1], reverse=descending)


def create_node_metrics_report(
    nodes: list[Node],
    threshold: float = DEFAULT_CPU_THRESHOLD,
) -> str:
    """Build a CPU report with nodes sorted from highest to lowest usage."""
    if not nodes:
        return "No nodes to report."

    average = sum(cpu_percent for _, cpu_percent in nodes) / len(nodes)
    overloaded_nodes = select_overloaded_nodes(nodes, threshold)
    sorted_nodes = sort_nodes_by_cpu(nodes)
    lines = [
        "Node metrics report",
        f"Total nodes: {len(nodes)}",
        f"Average CPU: {average:.1f}%",
        f"Overloaded nodes: {len(overloaded_nodes)}",
    ]

    for node_id, cpu_percent in sorted_nodes:
        state = "OVERLOADED" if cpu_percent > threshold else "NORMAL"
        lines.append(f"{node_id} | CPU: {cpu_percent:.1f}% | {state}")

    return "\n".join(lines)


def main() -> None:
    nodes = [
        ("node-1", 45.0),
        ("node-2", 92.5),
        ("node-3", 81.0),
        ("node-4", 67.5),
    ]
    print(create_node_metrics_report(nodes))


if __name__ == "__main__":
    main()
