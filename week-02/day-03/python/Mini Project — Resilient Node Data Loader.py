class InvalidNodeDataError(Exception):
    """Raised when node data is missing a required field."""
    pass


def validate_node(node):
    required_fields = ["id", "status", "cpu_usage"]
    for field in required_fields:
        if field not in node:
            raise InvalidNodeDataError(f"Node is missing required field: '{field}'")
        if field == "cpu_usage" and not isinstance(node["cpu_usage"], (int, float)):
            raise InvalidNodeDataError(f"Node '{node.get('id', '?')}' has non-numeric cpu_usage")
    return True


def load_nodes(raw_nodes):
    valid_nodes = []
    invalid_count = 0

    for node in raw_nodes:
        try:
            validate_node(node)
            valid_nodes.append(node)
        except InvalidNodeDataError as e:
            print(f"⚠️  Skipping invalid node: {e}")
            invalid_count += 1

    print(f"\n✅ Loaded {len(valid_nodes)} valid nodes")
    print(f"❌ Skipped {invalid_count} invalid nodes")
    return valid_nodes


if __name__ == "__main__":
    raw_nodes = [
        {"id": "node-1", "status": "active", "cpu_usage": 45},
        {"id": "node-2", "status": "active"},                       # missing cpu_usage
        {"id": "node-3", "status": "active", "cpu_usage": "high"},  # cpu_usage not numeric
        {"status": "active", "cpu_usage": 60},                       # missing id
        {"id": "node-5", "status": "inactive", "cpu_usage": 10},
    ]

    valid_nodes = load_nodes(raw_nodes)
    print("\nValid nodes:", valid_nodes)