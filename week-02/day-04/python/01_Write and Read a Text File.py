def write_log(filename, message):
    with open(filename, "w") as f:
        f.write(message)


def read_log(filename):
    with open(filename, "r") as f:
        return f.read()


write_log("sample.log", "Server started successfully.")
print(read_log("sample.log"))