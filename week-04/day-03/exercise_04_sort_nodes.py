"""Exercise 4: sort nodes by CPU usage in either direction."""

from node_metrics import Node, sort_nodes_by_cpu


def main() -> None:
    nodes: list[Node] = [
        ("node-1", 45.0),
        ("node-2", 92.5),
        ("node-3", 67.5),
    ]

    print("Highest CPU first:")
    for node in sort_nodes_by_cpu(nodes):
        print(node)

    print("\nLowest CPU first:")
    for node in sort_nodes_by_cpu(nodes, descending=False):
        print(node)


if __name__ == "__main__":
    main()
