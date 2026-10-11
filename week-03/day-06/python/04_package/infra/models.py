class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

    def __str__(self):
        return f"Node({self.id}, {self.status}, {self.cpu_usage}%)"