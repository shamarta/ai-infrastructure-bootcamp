"""Exercise 1: define and call a function with no parameters."""

from functions import get_gateway_status


if __name__ == "__main__":
    status = get_gateway_status()
    print(status)
