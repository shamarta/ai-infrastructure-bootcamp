"""Exercise 3: build data locally and return it to the caller."""


def get_overloaded_nodes(
    nodes: list[tuple[str, float]],
    threshold: float = 80.0,
) -> list[str]:
    overloaded_nodes = []

    for node_id, cpu_percent in nodes:
        if cpu_percent > threshold:
            overloaded_nodes.append(node_id)

    return overloaded_nodes


if __name__ == "__main__":
    cluster = [("node-1", 45.0), ("node-2", 91.0), ("node-3", 84.0)]
    overloaded = get_overloaded_nodes(cluster)
    print(f"Overloaded nodes: {overloaded}")
