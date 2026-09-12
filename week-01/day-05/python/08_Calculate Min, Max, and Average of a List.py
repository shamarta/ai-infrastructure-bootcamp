def calculate_stats(numbers):
    stats = {
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers)
    }
    return stats


print(calculate_stats([1, 2, 3, 4, 5]))
# {'min': 1, 'max': 5, 'average': 3.0}

print(calculate_stats([10, 20, 30]))
# {'min': 10, 'max': 30, 'average': 20.0}

print(calculate_stats([7]))
# {'min': 7, 'max': 7, 'average': 7.0}