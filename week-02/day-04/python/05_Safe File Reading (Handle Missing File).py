def safe_read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


print(safe_read_file("sample.log"))       # محتوای فایل
print(safe_read_file("missing.log"))      # None