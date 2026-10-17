"""Exercise 5: use a function that combines a loop and a condition."""

from functions import build_cluster_report


if __name__ == "__main__":
    cluster_nodes = [
        ("node-1", 45.0),
        ("node-2", 92.0),
        ("node-3", 70.0),
    ]

    print(build_cluster_report(cluster_nodes))
