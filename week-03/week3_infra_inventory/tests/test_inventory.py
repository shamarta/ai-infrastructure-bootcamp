import json

import pytest

from infra_inventory.inventory import Inventory
from infra_inventory.models import Node
from infra_inventory.providers import AzureProvider


@pytest.fixture
def inventory():
    inv = Inventory("test")
    inv.add(Node("node-1", "active", 45))
    inv.add(Node("node-2", "inactive", 0))
    inv.add(Node("node-3", "active", 88))
    inv.add(Node("node-4", "active", 92))
    return inv


def test_len_iter_and_contains(inventory):
    assert len(inventory) == 4
    assert "node-1" in inventory
    assert "nope" not in inventory
    assert [n.id for n in inventory] == ["node-1", "node-2", "node-3", "node-4"]


def test_duplicate_id_is_rejected(inventory):
    with pytest.raises(ValueError, match="duplicate"):
        inventory.add(Node("node-1", "active", 1))


def test_remove(inventory):
    removed = inventory.remove("node-2")
    assert removed.id == "node-2"
    assert len(inventory) == 3


def test_remove_missing_raises_keyerror(inventory):
    with pytest.raises(KeyError):
        inventory.remove("nope")


def test_active_nodes(inventory):
    assert [n.id for n in inventory.active_nodes()] == ["node-1", "node-3", "node-4"]


def test_overloaded_nodes_default_and_custom_threshold(inventory):
    assert [n.id for n in inventory.overloaded_nodes()] == ["node-3", "node-4"]
    assert [n.id for n in inventory.overloaded_nodes(threshold=90)] == ["node-4"]


def test_average_cpu_usage(inventory):
    assert inventory.average_cpu_usage() == pytest.approx((45 + 88 + 92) / 3)


def test_average_cpu_usage_is_none_without_active_nodes():
    inv = Inventory("empty")
    assert inv.average_cpu_usage() is None
    inv.add(Node("n", "inactive", 0))
    assert inv.average_cpu_usage() is None


def test_count_by_type(inventory):
    assert inventory.count_by_type() == {"Node": 4}


def test_from_json_loads_valid_and_records_invalid():
    payload = json.dumps(
        [
            {"id": "a", "type": "compute", "status": "active", "cpu_usage": 10},
            {"id": "b", "type": "storage", "status": "active", "cpu_usage": 20},
            {"id": "c", "type": "compute", "status": "active", "cpu_usage": 500},  # bad cpu
            {"id": "d", "type": "gpu", "status": "active", "cpu_usage": 5},        # bad type
            {"id": "a", "type": "compute", "status": "active", "cpu_usage": 1},    # duplicate id
            {"status": "active", "cpu_usage": 1},                                   # missing id
        ]
    )
    inv = Inventory.from_json("loaded", payload)
    assert len(inv) == 2
    assert inv.count_by_type() == {"ComputeNode": 1, "StorageNode": 1}
    assert len(inv.errors) == 4
    assert inv.errors[0].startswith("record 2:")


def test_from_json_rejects_malformed_json():
    with pytest.raises(ValueError):
        Inventory.from_json("bad", "{not json")


def test_from_json_rejects_non_list_root():
    with pytest.raises(ValueError, match="list"):
        Inventory.from_json("bad", '{"id": "a"}')


def test_provision_via_registers_the_node():
    inv = Inventory("cloud")
    node = inv.provision_via(AzureProvider(), "vm-1", "storage")
    assert "vm-1" in inv
    assert type(node).__name__ == "StorageNode"