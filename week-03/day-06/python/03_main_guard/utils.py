def greet(name):
    return f"Hello, {name}!"


print("utils.py: this line runs on import AND on direct execution")

if __name__ == "__main__":
    print("utils.py: this line runs ONLY when executed directly")
    print(greet("direct run"))