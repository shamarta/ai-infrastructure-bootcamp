"""Exercise 2: filter nodes with a conditional list comprehension."""

from infrastructure_inventory import Node, filter_nodes_by_cpu


def main() -> None:
    nodes: list[Node] = [
        ("api-1", "production", 72.0, 68.5),
        ("api-2", "production", 91.0, 76.0),
        ("worker-1", "staging", 64.5, 88.0),
    ]
    print(filter_nodes_by_cpu(nodes, threshold=80.0))


if __name__ == "__main__":
    main()
