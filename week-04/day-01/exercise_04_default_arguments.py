"""Exercise 4: call a function with default and named arguments."""

from functions import is_overloaded


if __name__ == "__main__":
    print(f"CPU 85% with default threshold: {is_overloaded(85.0)}")
    print(
        "CPU 75% with custom threshold: "
        f"{is_overloaded(75.0, threshold=70.0)}"
    )
