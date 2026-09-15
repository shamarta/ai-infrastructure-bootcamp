"""
test_node_monitor.py

Unit tests for node_monitor.py using pytest.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from node_monitor import (
    get_unique_active_ips,
    get_high_load_nodes,
    get_inactive_node_ids,
    has_duplicate_ips,
    average_cpu_usage,
    get_active_cpu_map,
    get_node_summary,
)

SAMPLE_NODES = [
    {"id": "node-1", "ip": "192.168.1.10", "status": "active", "cpu_usage": 45},
    {"id": "node-2", "ip": "192.168.1.11", "status": "inactive", "cpu_usage": 0},
    {"id": "node-3", "ip": "192.168.1.10", "status": "active", "cpu_usage": 88},
    {"id": "node-4", "ip": "192.168.1.12", "status": "active", "cpu_usage": 92},
]


def test_get_unique_active_ips():
    result = get_unique_active_ips(SAMPLE_NODES)
    assert result == {"192.168.1.10", "192.168.1.12"}


def test_get_high_load_nodes_default_threshold():
    result = get_high_load_nodes(SAMPLE_NODES)
    assert result == ["node-3", "node-4"]


def test_get_high_load_nodes_custom_threshold():
    result = get_high_load_nodes(SAMPLE_NODES, threshold=50)
    assert result == ["node-3", "node-4"]


def test_get_inactive_node_ids():
    result = get_inactive_node_ids(SAMPLE_NODES)
    assert result == ["node-2"]


def test_has_duplicate_ips_true():
    assert has_duplicate_ips(SAMPLE_NODES) is True


def test_has_duplicate_ips_false():
    unique_nodes = [
        {"id": "node-1", "ip": "10.0.0.1", "status": "active", "cpu_usage": 10},
        {"id": "node-2", "ip": "10.0.0.2", "status": "active", "cpu_usage": 20},
    ]
    assert has_duplicate_ips(unique_nodes) is False


def test_average_cpu_usage_normal_case():
    result = average_cpu_usage(SAMPLE_NODES)
    assert result == 75.0


def test_average_cpu_usage_no_active_nodes():
    all_inactive = [
        {"id": "node-1", "ip": "10.0.0.1", "status": "inactive", "cpu_usage": 0},
    ]
    assert average_cpu_usage(all_inactive) is None


def test_average_cpu_usage_empty_list():
    assert average_cpu_usage([]) is None


def test_get_active_cpu_map():
    result = get_active_cpu_map(SAMPLE_NODES)
    assert result == {"node-1": 45, "node-3": 88, "node-4": 92}


def test_get_node_summary():
    result = get_node_summary(SAMPLE_NODES)
    assert result["total_nodes"] == 4
    assert result["active_count"] == 3
    assert result["inactive_count"] == 1
    assert result["unique_ips"] == 2
    assert result["avg_active_cpu"] == 75.0