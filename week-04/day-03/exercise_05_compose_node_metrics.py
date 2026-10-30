"""Exercise 5: combine map, filter, and sorted in a node report."""

from node_metrics import Node, create_node_metrics_report


def main() -> None:
    nodes: list[Node] = [
        ("node-1", 45.0),
        ("node-2", 92.5),
        ("node-3", 81.0),
    ]
    print(create_node_metrics_report(nodes, threshold=80.0))


if __name__ == "__main__":
    main()
