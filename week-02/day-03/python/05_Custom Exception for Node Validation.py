class InvalidNodeDataError(Exception):
    """Raised when node data is missing a required field."""
    pass


def validate_node(node):
    required_fields = ["id", "status", "cpu_usage"]
    for field in required_fields:
        if field not in node:
            raise InvalidNodeDataError(f"Node is missing required field: '{field}'")
    return True


# Test cases
valid_node = {"id": "node-1", "status": "active", "cpu_usage": 45}
invalid_node = {"id": "node-2", "status": "active"}  # cpu_usage missing

print(validate_node(valid_node))   # True

try:
    validate_node(invalid_node)
except InvalidNodeDataError as e:
    print(f"Validation failed: {e}")