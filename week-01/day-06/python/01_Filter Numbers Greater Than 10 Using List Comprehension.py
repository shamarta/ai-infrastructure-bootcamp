def filter_greater_than_10(numbers):
    # Keep only the numbers greater than 10
    return [num for num in numbers if num > 10]

numbers = [5, 12, 8, 20, 3, 15]
print(filter_greater_than_10(numbers))  # [12, 20, 15]