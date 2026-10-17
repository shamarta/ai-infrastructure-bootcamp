from functions import (
    average_cpu_usage,
    build_cluster_report,
    format_node_summary,
    get_gateway_status,
    is_overloaded,
)


def test_get_gateway_status() -> None:
    assert get_gateway_status() == "Gateway is running."


def test_is_overloaded_uses_default_threshold() -> None:
    assert is_overloaded(85.0) is True
    assert is_overloaded(80.0) is False
    assert is_overloaded(40.0) is False


def test_is_overloaded_accepts_custom_threshold() -> None:
    assert is_overloaded(75.0, threshold=70.0) is True
    assert is_overloaded(65.0, threshold=70.0) is False


def test_average_cpu_usage_returns_average() -> None:
    assert average_cpu_usage([20.0, 40.0, 60.0]) == 40.0


def test_average_cpu_usage_returns_none_for_empty_list() -> None:
    assert average_cpu_usage([]) is None


def test_format_node_summary() -> None:
    result = format_node_summary("node-1", "active", 45.0)

    assert result == "node-1 | active | CPU: 45.0%"


def test_build_cluster_report_marks_overloaded_nodes() -> None:
    result = build_cluster_report(
        [("node-1", 45.0), ("node-2", 90.0)],
    )

    assert result == (
        "node-1 | active | CPU: 45.0%\n"
        "node-2 | active | CPU: 90.0% | OVERLOADED"
    )


def test_build_cluster_report_accepts_custom_threshold() -> None:
    result = build_cluster_report([("node-1", 75.0)], threshold=70.0)

    assert result == "node-1 | active | CPU: 75.0% | OVERLOADED"


def test_build_cluster_report_handles_empty_nodes() -> None:
    assert build_cluster_report([]) == "No nodes to report."