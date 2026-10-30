"""Exercise 2: transform each CPU value with map."""

from node_metrics import format_cpu_usages


def main() -> None:
    cpu_usages = [45.0, 92.5, 67.5]
    formatted_usages = format_cpu_usages(cpu_usages)
    print(formatted_usages)


if __name__ == "__main__":
    main()
