class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

    @property
    def is_healthy(self):
        return self.status == "active" and self.cpu_usage < 80


node = Node("node-1", "active", 45)
print(node.is_healthy)    # True

node.cpu_usage = 95
print(node.is_healthy)    # False — چون دوباره محاسبه شد، نه یک مقدار ذخیره‌شده‌ی قدیمی