"""Infrastructure-related function exercises."""


def get_gateway_status() -> str:
    """Return a simple status message for the gateway."""
    return "Gateway is running."


def is_overloaded(
    cpu_percent: float,
    threshold: float = 80.0,
) -> bool:
    """Return whether CPU usage is above the threshold."""
    return cpu_percent > threshold


def average_cpu_usage(usages: list[float]) -> float | None:
    """Return the average CPU usage, or None when there are no values."""
    if not usages:
        return None

    return sum(usages) / len(usages)


def format_node_summary(
    node_id: str,
    status: str,
    cpu_percent: float,
) -> str:
    """Return a readable one-line summary for an infrastructure node."""
    return f"{node_id} | {status} | CPU: {cpu_percent:.1f}%"


def build_cluster_report(
    nodes: list[tuple[str, float]],
    threshold: float = 80.0,
) -> str:
    """Return a report showing each node and whether its CPU is overloaded."""
    if not nodes:
        return "No nodes to report."

    report_lines = []
    for node_id, cpu_percent in nodes:
        summary = format_node_summary(node_id, "active", cpu_percent)
        if is_overloaded(cpu_percent, threshold):
            summary += " | OVERLOADED"
        report_lines.append(summary)

    return "\n".join(report_lines)