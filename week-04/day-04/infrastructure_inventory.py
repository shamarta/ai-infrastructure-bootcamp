"""Comprehension-based helpers for reporting infrastructure inventory."""

DEFAULT_CPU_THRESHOLD = 80.0
DEFAULT_MEMORY_THRESHOLD = 85.0
Node = tuple[str, str, float, float]


def get_node_names(nodes: list[Node]) -> list[str]:
    """Return the names of all nodes in inventory order."""
    return [name for name, _, _, _ in nodes]


def filter_nodes_by_cpu(
    nodes: list[Node],
    threshold: float = DEFAULT_CPU_THRESHOLD,
) -> list[Node]:
    """Return nodes whose CPU usage is above the threshold."""
    return [node for node in nodes if node[2] > threshold]


def format_inventory(nodes: list[Node]) -> list[str]:
    """Format each inventory record as a readable line."""
    return [
        f"{name} | Environment: {environment} | "
        f"CPU: {cpu:.1f}% | Memory: {memory:.1f}%"
        for name, environment, cpu, memory in nodes
    ]


def build_node_statuses(
    nodes: list[Node],
    cpu_threshold: float = DEFAULT_CPU_THRESHOLD,
    memory_threshold: float = DEFAULT_MEMORY_THRESHOLD,
) -> dict[str, str]:
    """Map each node name to NORMAL or ALERT based on resource thresholds."""
    return {
        name: (
            "ALERT"
            if cpu > cpu_threshold or memory > memory_threshold
            else "NORMAL"
        )
        for name, _, cpu, memory in nodes
    }


def group_nodes_by_environment(nodes: list[Node]) -> dict[str, list[str]]:
    """Group node names under their environments using a nested comprehension."""
    environments = list(dict.fromkeys(environment for _, environment, _, _ in nodes))
    return {
        environment: [
            name for name, node_environment, _, _ in nodes
            if node_environment == environment
        ]
        for environment in environments
    }


def create_inventory_report(
    nodes: list[Node],
    cpu_threshold: float = DEFAULT_CPU_THRESHOLD,
    memory_threshold: float = DEFAULT_MEMORY_THRESHOLD,
) -> str:
    """Build an inventory summary and list the status of each node."""
    if not nodes:
        return "No nodes to report."

    statuses = build_node_statuses(nodes, cpu_threshold, memory_threshold)
    average_cpu = sum(cpu for _, _, cpu, _ in nodes) / len(nodes)
    average_memory = sum(memory for _, _, _, memory in nodes) / len(nodes)
    alert_count = sum(status == "ALERT" for status in statuses.values())
    lines = [
        "Infrastructure inventory report",
        f"Total nodes: {len(nodes)}",
        f"Average CPU: {average_cpu:.1f}%",
        f"Average memory: {average_memory:.1f}%",
        f"Nodes requiring attention: {alert_count}",
    ]

    lines.extend(
        f"{name} | Environment: {environment} | "
        f"CPU: {cpu:.1f}% | Memory: {memory:.1f}% | {statuses[name]}"
        for name, environment, cpu, memory in nodes
    )
    return "\n".join(lines)


def main() -> None:
    nodes: list[Node] = [
        ("api-1", "production", 72.0, 68.5),
        ("api-2", "production", 91.0, 76.0),
        ("worker-1", "staging", 64.5, 88.0),
        ("db-1", "production", 78.0, 79.5),
    ]
    print(create_inventory_report(nodes))


if __name__ == "__main__":
    main()
