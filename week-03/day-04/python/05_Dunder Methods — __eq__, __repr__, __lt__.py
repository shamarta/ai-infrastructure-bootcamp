class Node:
    def __init__(self, node_id, cpu_usage):
        self.id = node_id
        self.cpu_usage = cpu_usage

    def __eq__(self, other):
        return self.id == other.id          # دو node با id یکسان، برابر حساب می‌شن

    def __lt__(self, other):
        return self.cpu_usage < other.cpu_usage   # برای مرتب‌سازی بر اساس CPU

    def __repr__(self):
        return f"Node(id={self.id!r}, cpu_usage={self.cpu_usage})"


a = Node("node-1", 45)
b = Node("node-1", 90)
c = Node("node-2", 30)

print(a == b)         # True (id یکسان)
print(a == c)         # False
print(c < a)          # True (۳۰ < ۴۵)

nodes = [a, c, Node("node-3", 70)]
print(sorted(nodes))  # بر اساس cpu_usage مرتب می‌شه، بدون نیاز به key=