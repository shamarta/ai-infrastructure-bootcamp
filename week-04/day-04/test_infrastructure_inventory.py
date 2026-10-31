from infrastructure_inventory import (
    build_node_statuses,
    create_inventory_report,
    filter_nodes_by_cpu,
    format_inventory,
    get_node_names,
    group_nodes_by_environment,
)


def test_get_node_names_preserves_inventory_order() -> None:
    nodes = [
        ("api-1", "production", 72.0, 68.5),
        ("worker-1", "staging", 64.5, 88.0),
    ]

    assert get_node_names(nodes) == ["api-1", "worker-1"]


def test_get_node_names_handles_empty_inventory() -> None:
    assert get_node_names([]) == []


def test_filter_nodes_by_cpu_uses_strict_threshold() -> None:
    nodes = [
        ("api-1", "production", 80.0, 70.0),
        ("api-2", "production", 80.1, 70.0),
        ("worker-1", "staging", 95.0, 50.0),
    ]

    assert filter_nodes_by_cpu(nodes) == [nodes[1], nodes[2]]


def test_filter_nodes_by_cpu_accepts_custom_threshold() -> None:
    nodes = [
        ("api-1", "production", 75.0, 70.0),
        ("api-2", "production", 65.0, 70.0),
    ]

    assert filter_nodes_by_cpu(nodes, threshold=70.0) == [nodes[0]]


def test_format_inventory_formats_each_record() -> None:
    assert format_inventory([("api-1", "production", 72.04, 68.56)]) == [
        "api-1 | Environment: production | CPU: 72.0% | Memory: 68.6%"
    ]


def test_build_node_statuses_checks_both_thresholds() -> None:
    nodes = [
        ("normal", "production", 80.0, 85.0),
        ("cpu-alert", "production", 80.1, 60.0),
        ("memory-alert", "staging", 60.0, 85.1),
    ]

    assert build_node_statuses(nodes) == {
        "normal": "NORMAL",
        "cpu-alert": "ALERT",
        "memory-alert": "ALERT",
    }


def test_build_node_statuses_accepts_custom_thresholds() -> None:
    nodes = [("api-1", "production", 71.0, 70.0)]

    assert build_node_statuses(
        nodes,
        cpu_threshold=70.0,
        memory_threshold=75.0,
    ) == {"api-1": "ALERT"}


def test_group_nodes_by_environment_keeps_input_and_group_order() -> None:
    nodes = [
        ("api-1", "production", 72.0, 68.5),
        ("worker-1", "staging", 64.5, 88.0),
        ("api-2", "production", 91.0, 76.0),
    ]

    assert group_nodes_by_environment(nodes) == {
        "production": ["api-1", "api-2"],
        "staging": ["worker-1"],
    }


def test_group_nodes_by_environment_handles_empty_inventory() -> None:
    assert group_nodes_by_environment([]) == {}


def test_create_inventory_report_includes_averages_and_statuses() -> None:
    report = create_inventory_report(
        [
            ("api-1", "production", 72.0, 68.0),
            ("api-2", "production", 91.0, 76.0),
        ]
    )

    assert report == (
        "Infrastructure inventory report\n"
        "Total nodes: 2\n"
        "Average CPU: 81.5%\n"
        "Average memory: 72.0%\n"
        "Nodes requiring attention: 1\n"
        "api-1 | Environment: production | CPU: 72.0% | Memory: 68.0% | NORMAL\n"
        "api-2 | Environment: production | CPU: 91.0% | Memory: 76.0% | ALERT"
    )


def test_create_inventory_report_accepts_custom_thresholds() -> None:
    report = create_inventory_report(
        [("api-1", "production", 71.0, 70.0)],
        cpu_threshold=70.0,
        memory_threshold=75.0,
    )

    assert "Nodes requiring attention: 1" in report
    assert report.endswith(
        "api-1 | Environment: production | CPU: 71.0% | "
        "Memory: 70.0% | ALERT"
    )


def test_create_inventory_report_handles_empty_inventory() -> None:
    assert create_inventory_report([]) == "No nodes to report."
