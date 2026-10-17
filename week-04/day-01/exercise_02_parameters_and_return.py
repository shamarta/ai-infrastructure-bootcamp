"""Exercise 2: pass arguments and use a function's returned value."""

from functions import format_node_summary


if __name__ == "__main__":
    summary = format_node_summary("node-1", "active", 45.0)
    print(summary)
