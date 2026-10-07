class Node:
    def __init__(self, node_id, cpu_usage):
        self.id = node_id
        self.cpu_usage = cpu_usage   # این در واقع setter رو صدا می‌زنه

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


node = Node("node-1", 45)
print(node.cpu_usage)     # 45

node.cpu_usage = 90       # ✅ مجازه، چون معتبره
print(node.cpu_usage)

node.cpu_usage = 150      # ❌ ValueError: cpu_usage must be between 0 and 100