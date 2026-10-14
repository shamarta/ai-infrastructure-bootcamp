import pytest

from infra_inventory.models import ComputeNode, Node, StorageNode, node_from_dict


def test_valid_node_is_created():
    node = Node("node-1", "active", 45)
    assert node.id == "node-1"
    assert node.status == "active"
    assert node.cpu_usage == 45


def test_invalid_status_is_rejected():
    with pytest.raises(ValueError, match="status must be one of"):
        Node("node-1", "exploded", 10)


@pytest.mark.parametrize("bad_value", [-1, 101, 150])
def test_cpu_out_of_range_is_rejected(bad_value):
    with pytest.raises(ValueError, match="between 0 and 100"):
        Node("node-1", "active", bad_value)


@pytest.mark.parametrize("bad_value", ["high", None, True])
def test_non_numeric_cpu_is_rejected(bad_value):
    with pytest.raises(TypeError):
        Node("node-1", "active", bad_value)


@pytest.mark.parametrize(
    "status, cpu, expected",
    [
        ("active", 90, True),
        ("active", 80, False),   # threshold is exclusive
        ("active", 10, False),
        ("inactive", 99, False),  # inactive nodes are never "overloaded"
    ],
)
def test_is_overloaded(status, cpu, expected):
    assert Node("n", status, cpu).is_overloaded() is expected


def test_is_overloaded_custom_threshold():
    assert Node("n", "active", 60).is_overloaded(threshold=50) is True


def test_resource_summary_is_polymorphic():
    assert Node("n", "active", 1).resource_summary() == "no specific resources"
    assert ComputeNode("n", "active", 1, cpu_cores=8, memory_gb=32).resource_summary() == "8 vCPUs, 32GB RAM"
    assert StorageNode("n", "active", 1, capacity_gb=500).resource_summary() == "500GB storage"


def test_subclass_is_still_a_node():
    assert isinstance(ComputeNode("n", "active", 1), Node)


def test_dataclass_equality():
    assert Node("a", "active", 5) == Node("a", "active", 5)
    assert Node("a", "active", 5) != Node("b", "active", 5)


def test_node_from_dict_builds_the_right_subclass():
    compute = node_from_dict({"id": "c", "type": "compute", "status": "active", "cpu_usage": 5, "cpu_cores": 4})
    storage = node_from_dict({"id": "s", "type": "storage", "status": "active", "cpu_usage": 5})
    generic = node_from_dict({"id": "g", "status": "active", "cpu_usage": 5})
    assert type(compute) is ComputeNode and compute.cpu_cores == 4
    assert type(storage) is StorageNode
    assert type(generic) is Node


def test_node_from_dict_does_not_mutate_input():
    data = {"id": "c", "type": "compute", "status": "active", "cpu_usage": 5}
    node_from_dict(data)
    assert "type" in data


def test_node_from_dict_unknown_type():
    with pytest.raises(ValueError, match="unknown node type"):
        node_from_dict({"id": "x", "type": "gpu", "status": "active", "cpu_usage": 1})


def test_node_from_dict_missing_field():
    with pytest.raises(TypeError):
        node_from_dict({"id": "x", "status": "active"})  # cpu_usage missing