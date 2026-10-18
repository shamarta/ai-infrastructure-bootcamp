"""Exercise 4: pass configuration instead of changing global state."""

DEFAULT_CPU_THRESHOLD = 80.0


def is_overloaded(
    cpu_percent: float,
    threshold: float = DEFAULT_CPU_THRESHOLD,
) -> bool:
    return cpu_percent > threshold


if __name__ == "__main__":
    print(f"Default threshold: {is_overloaded(85.0)}")
    print(f"Custom threshold: {is_overloaded(75.0, threshold=70.0)}")
    print(f"Default remains unchanged: {DEFAULT_CPU_THRESHOLD}")
