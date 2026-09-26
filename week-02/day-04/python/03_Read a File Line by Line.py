def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


lines = read_lines("sample.log")
print(lines)