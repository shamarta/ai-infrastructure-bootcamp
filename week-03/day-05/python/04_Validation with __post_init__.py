from dataclasses import dataclass


@dataclass
class Node:
    id: str
    status: str
    cpu_usage: int

    def __post_init__(self):
        # بعد از ساخته شدن شیء خودکار اجرا می‌شه
        if not (0 <= self.cpu_usage <= 100):
            raise ValueError(f"cpu_usage must be 0-100, got {self.cpu_usage}")


good = Node("node-1", "active", 45)
print(good)

try:
    bad = Node("node-2", "active", 150)
except ValueError as e:
    print(f"❌ {e}")