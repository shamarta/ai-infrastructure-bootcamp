"""Exercise 1: extract node names with a list comprehension."""

from infrastructure_inventory import Node, get_node_names


def main() -> None:
    nodes: list[Node] = [
        ("api-1", "production", 72.0, 68.5),
        ("worker-1", "staging", 64.5, 88.0),
    ]
    print(get_node_names(nodes))


if __name__ == "__main__":
    main()
