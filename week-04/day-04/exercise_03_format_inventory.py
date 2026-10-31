"""Exercise 3: transform node records with a list comprehension."""

from infrastructure_inventory import Node, format_inventory


def main() -> None:
    nodes: list[Node] = [
        ("api-1", "production", 72.0, 68.5),
        ("worker-1", "staging", 64.5, 88.0),
    ]
    print("\n".join(format_inventory(nodes)))


if __name__ == "__main__":
    main()
