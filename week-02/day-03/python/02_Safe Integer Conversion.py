def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None


print(safe_int("42"))       # 42
print(safe_int("abc"))      # None
print(safe_int("3.14"))     # None 