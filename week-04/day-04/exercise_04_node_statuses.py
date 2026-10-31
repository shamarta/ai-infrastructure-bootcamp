"""Exercise 4: create a node status dictionary with a dictionary comprehension."""

from infrastructure_inventory import Node, build_node_statuses


def main() -> None:
    nodes: list[Node] = [
        ("api-1", "production", 72.0, 68.5),
        ("api-2", "production", 91.0, 76.0),
        ("worker-1", "staging", 64.5, 88.0),
    ]
    print(build_node_statuses(nodes))


if __name__ == "__main__":
    main()
