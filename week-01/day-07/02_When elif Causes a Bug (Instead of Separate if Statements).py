def check_character(char):
    # BUGGY VERSION: using elif when conditions are NOT mutually exclusive
    result = {"is_alpha": False, "is_upper": False}

    if char.isalpha():
        result["is_alpha"] = True
    elif char.isupper():          # This line will almost never run!
        result["is_upper"] = True

    return result


# A capital letter IS both alpha AND upper — but elif skips the second check
print(check_character("A"))
# Output: {'is_alpha': True, 'is_upper': False}  <-- BUG: is_upper should be True!


def check_character_fixed(char):
    # FIXED VERSION: independent conditions each get their own `if`
    result = {"is_alpha": False, "is_upper": False}

    if char.isalpha():
        result["is_alpha"] = True
    if char.isupper():
        result["is_upper"] = True

    return result


print(check_character_fixed("A"))
# Output: {'is_alpha': True, 'is_upper': True}  <-- Correct