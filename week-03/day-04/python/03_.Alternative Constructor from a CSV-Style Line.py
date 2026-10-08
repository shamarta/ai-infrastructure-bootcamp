class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(",")
        return cls(parts[0], parts[1], int(parts[2]))

    def __str__(self):
        return f"Node({self.id}, {self.status}, {self.cpu_usage}%)"


node = Node.from_csv_line("node-2,inactive,0")
print(node)   # Node(node-2, inactive, 0%)