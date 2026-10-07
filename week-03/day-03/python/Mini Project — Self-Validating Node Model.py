class Node:
    VALID_STATUSES = ("active", "inactive", "maintenance")

    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status       # از setter عبور می‌کنه
        self.cpu_usage = cpu_usage  # از setter عبور می‌کنه

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"status must be one of {self.VALID_STATUSES}")
        self._status = value

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

    def __str__(self):
        return f"Node({self.id}, {self.status}, {self.cpu_usage}%)"


def try_update(node, field, value):
    try:
        setattr(node, field, value)
        print(f"✅ {field} updated to {value}")
    except (TypeError, ValueError) as e:
        print(f"❌ Failed to update {field} to {value}: {e}")


if __name__ == "__main__":
    node = Node("node-1", "active", 45)
    print(node, "| overloaded:", node.is_overloaded)

    try_update(node, "cpu_usage", 90)
    print(node, "| overloaded:", node.is_overloaded)

    try_update(node, "cpu_usage", -10)        # نامعتبر
    try_update(node, "cpu_usage", "high")      # نامعتبر
    try_update(node, "status", "unknown")      # نامعتبر
    try_update(node, "status", "maintenance")  # معتبر

    print(node, "| overloaded:", node.is_overloaded)