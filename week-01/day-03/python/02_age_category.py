age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child")

elif age <= 17:
    print("You are a Teenager")

elif age <= 64:
    print("You are an Adult")

else:
    print("You are a Senior")