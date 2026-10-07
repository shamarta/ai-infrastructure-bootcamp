class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage   # از setter عبور می‌کنه

    @property
    def cpu_usage(self):
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("cpu_usage must be a number")
        if not (0 <= value <= 100):
            raise ValueError("cpu_usage must be between 0 and 100")
        self._cpu_usage = value

    @property
    def is_overloaded(self):
        return self.status == "active" and self.cpu_usage > 80


node = Node("node-1", "active", 45)
print(node.is_overloaded)   # False

node.cpu_usage = 95
print(node.is_overloaded)   # True

try:
    node.cpu_usage = "very high"
except TypeError as e:
    print(f"Rejected: {e}")