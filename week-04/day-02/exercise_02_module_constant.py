"""Exercise 2: read a module-level constant inside a function."""

DEFAULT_CPU_THRESHOLD = 80.0


def is_overloaded(cpu_percent: float) -> bool:
    return cpu_percent > DEFAULT_CPU_THRESHOLD


if __name__ == "__main__":
    print(is_overloaded(92.0))
    print(is_overloaded(65.0))
