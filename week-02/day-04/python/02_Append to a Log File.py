def append_log(filename, message):
    with open(filename, "a") as f:
        f.write(message + "\n")


append_log("sample.log", "New connection from node-2")
append_log("sample.log", "Health check passed")
def read_log(filename):
    with open(filename, "r") as f:
        return f.read()

print(read_log("sample.log"))