"""Exercise 1: observe a variable that belongs to a function's local scope."""


def get_node_message(node_id: str) -> str:
    message = f"Node {node_id} is ready."
    return message


if __name__ == "__main__":
    result = get_node_message("node-1")
    print(result)
