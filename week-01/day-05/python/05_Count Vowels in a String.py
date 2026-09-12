def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, World!"))  # Output: 3
print(count_vowels("Python is awesome!"))  # Output: 6  
print(count_vowels("shamarta"))  # Output: 3