"""Exercise 1: use a lambda as a sorting key."""

from node_metrics import Node, sort_nodes_by_cpu


def main() -> None:
    nodes: list[Node] = [
        ("node-1", 45.0),
        ("node-2", 92.5),
        ("node-3", 67.5),
    ]

    for node in sort_nodes_by_cpu(nodes):
        print(node)


if __name__ == "__main__":
    main()
