from mini_project_cluster_report import (
    average_cpu_usage,
    create_cluster_report,
    format_node_line,
    is_overloaded,
)


def test_is_overloaded_uses_strict_threshold() -> None:
    assert is_overloaded(81.0, 80.0) is True
    assert is_overloaded(80.0, 80.0) is False


def test_average_cpu_usage_returns_average() -> None:
    assert average_cpu_usage([("node-1", 40.0), ("node-2", 60.0)]) == 50.0


def test_average_cpu_usage_returns_none_for_empty_nodes() -> None:
    assert average_cpu_usage([]) is None


def test_format_node_line_marks_overloaded_node() -> None:
    assert format_node_line("node-1", 90.0, 80.0) == (
        "node-1 | CPU: 90.0% | OVERLOADED"
    )


def test_create_cluster_report_includes_average_and_node_states() -> None:
    report = create_cluster_report(
        [("node-1", 40.0), ("node-2", 90.0)],
    )

    assert report == (
        "Cluster health report\n"
        "Nodes: 2\n"
        "Average CPU: 65.0%\n"
        "node-1 | CPU: 40.0% | NORMAL\n"
        "node-2 | CPU: 90.0% | OVERLOADED"
    )


def test_create_cluster_report_handles_empty_cluster() -> None:
    assert create_cluster_report([]) == "No nodes to report."


def test_create_cluster_report_accepts_custom_threshold() -> None:
    report = create_cluster_report([("node-1", 75.0)], threshold=70.0)

    assert report.endswith("node-1 | CPU: 75.0% | OVERLOADED")
