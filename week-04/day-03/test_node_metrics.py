from node_metrics import (
    create_node_metrics_report,
    format_cpu_usages,
    select_overloaded_nodes,
    sort_nodes_by_cpu,
)


def test_format_cpu_usages_formats_each_value() -> None:
    assert format_cpu_usages([45.0, 92.56]) == ["45.0%", "92.6%"]


def test_format_cpu_usages_handles_empty_list() -> None:
    assert format_cpu_usages([]) == []


def test_select_overloaded_nodes_uses_strict_threshold() -> None:
    nodes = [("node-1", 80.0), ("node-2", 80.1), ("node-3", 95.0)]

    assert select_overloaded_nodes(nodes) == [
        ("node-2", 80.1),
        ("node-3", 95.0),
    ]


def test_select_overloaded_nodes_accepts_custom_threshold() -> None:
    assert select_overloaded_nodes(
        [("node-1", 75.0), ("node-2", 65.0)],
        threshold=70.0,
    ) == [("node-1", 75.0)]


def test_sort_nodes_by_cpu_defaults_to_descending() -> None:
    nodes = [("node-1", 45.0), ("node-2", 92.5), ("node-3", 67.5)]

    assert sort_nodes_by_cpu(nodes) == [
        ("node-2", 92.5),
        ("node-3", 67.5),
        ("node-1", 45.0),
    ]


def test_sort_nodes_by_cpu_can_sort_ascending() -> None:
    nodes = [("node-1", 45.0), ("node-2", 92.5), ("node-3", 67.5)]

    assert sort_nodes_by_cpu(nodes, descending=False) == [
        ("node-1", 45.0),
        ("node-3", 67.5),
        ("node-2", 92.5),
    ]


def test_create_node_metrics_report_sorts_and_classifies_nodes() -> None:
    report = create_node_metrics_report(
        [("node-1", 45.0), ("node-2", 92.5), ("node-3", 81.0)],
    )

    assert report == (
        "Node metrics report\n"
        "Total nodes: 3\n"
        "Average CPU: 72.8%\n"
        "Overloaded nodes: 2\n"
        "node-2 | CPU: 92.5% | OVERLOADED\n"
        "node-3 | CPU: 81.0% | OVERLOADED\n"
        "node-1 | CPU: 45.0% | NORMAL"
    )


def test_create_node_metrics_report_accepts_custom_threshold() -> None:
    report = create_node_metrics_report(
        [("node-1", 75.0), ("node-2", 65.0)],
        threshold=70.0,
    )

    assert "Overloaded nodes: 1" in report
    assert report.endswith(
        "node-1 | CPU: 75.0% | OVERLOADED\n"
        "node-2 | CPU: 65.0% | NORMAL"
    )


def test_create_node_metrics_report_handles_empty_cluster() -> None:
    assert create_node_metrics_report([]) == "No nodes to report."
