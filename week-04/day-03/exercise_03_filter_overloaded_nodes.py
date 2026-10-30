"""Exercise 3: select nodes above a CPU threshold with filter."""

from node_metrics import Node, select_overloaded_nodes


def main() -> None:
    nodes: list[Node] = [
        ("node-1", 45.0),
        ("node-2", 92.5),
        ("node-3", 81.0),
    ]

    print(select_overloaded_nodes(nodes))


if __name__ == "__main__":
    main()
