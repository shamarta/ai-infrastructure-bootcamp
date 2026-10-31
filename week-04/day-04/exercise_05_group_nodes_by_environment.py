"""Exercise 5: group node names by environment with a nested comprehension."""

from infrastructure_inventory import Node, group_nodes_by_environment


def main() -> None:
    nodes: list[Node] = [
        ("api-1", "production", 72.0, 68.5),
        ("worker-1", "staging", 64.5, 88.0),
        ("api-2", "production", 91.0, 76.0),
    ]
    print(group_nodes_by_environment(nodes))


if __name__ == "__main__":
    main()
