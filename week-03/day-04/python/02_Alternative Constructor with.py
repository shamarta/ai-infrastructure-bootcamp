class Node:
    def __init__(self, node_id, status, cpu_usage):
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["status"], data["cpu_usage"])

    def __str__(self):
        return f"Node({self.id}, {self.status}, {self.cpu_usage}%)"


api_data = {"id": "node-1", "status": "active", "cpu_usage": 45}
node = Node.from_dict(api_data)
print(node)   # Node(node-1, active, 45%)