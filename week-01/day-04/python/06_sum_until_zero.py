number = int(input("Enter a number: "))

total = 0

while number != 0:
    total += number
    number = int(input("Enter another number: "))

print(f"Total: {total}")