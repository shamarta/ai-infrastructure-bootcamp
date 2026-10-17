"""Exercise 3: distinguish a returned value from printed output."""

from functions import average_cpu_usage


if __name__ == "__main__":
    average = average_cpu_usage([20.0, 40.0, 60.0])
    print(f"Returned value: {average}")

    empty_average = average_cpu_usage([])
    print(f"Returned value for an empty list: {empty_average}")
