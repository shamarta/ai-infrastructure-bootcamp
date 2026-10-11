from dataclasses import dataclass


@dataclass
class Node:
    id: str
    status: str
    cpu_usage: int

    def __post_init__(self):
        if not (0 <= self.cpu_usage <= 100):
            raise ValueError(f"cpu_usage must be 0-100, got {self.cpu_usage}")

    @property
    def is_overloaded(self):
        return self.status == "active" and self.cpu_usage > 80