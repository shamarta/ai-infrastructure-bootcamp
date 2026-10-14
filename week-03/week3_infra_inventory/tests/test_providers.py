import pytest

from infra_inventory.models import ComputeNode, Node
from infra_inventory.providers import AWSProvider, AzureProvider, CloudProvider


def test_abstract_base_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        CloudProvider()


def test_incomplete_subclass_cannot_be_instantiated():
    class BrokenProvider(CloudProvider):
        name = "broken"

        def provision(self, node_id, node_type="compute"):
            return Node(node_id, "active", 0)
        # decommission is missing

    with pytest.raises(TypeError):
        BrokenProvider()


@pytest.mark.parametrize("provider_class", [AzureProvider, AWSProvider])
def test_provision_returns_an_active_node(provider_class):
    node = provider_class().provision("web-1")
    assert isinstance(node, ComputeNode)
    assert node.id == "web-1"
    assert node.status == "active"


@pytest.mark.parametrize("provider_class", [AzureProvider, AWSProvider])
def test_decommission_deactivates_the_node(provider_class):
    provider = provider_class()
    node = provider.provision("web-1")
    message = provider.decommission(node)
    assert node.status == "inactive"
    assert "web-1" in message


def test_providers_word_their_messages_differently():
    azure_msg = AzureProvider().decommission(AzureProvider().provision("a"))
    aws_msg = AWSProvider().decommission(AWSProvider().provision("a"))
    assert azure_msg != aws_msg