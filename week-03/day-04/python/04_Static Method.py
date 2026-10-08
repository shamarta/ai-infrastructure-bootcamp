class Node:
    def __init__(self, node_id, cpu_usage):
        self.id = node_id
        self.cpu_usage = cpu_usage

    @staticmethod
    def is_valid_cpu(value):
        return isinstance(value, (int, float)) and 0 <= value <= 100


print(Node.is_valid_cpu(45))      # True
print(Node.is_valid_cpu(150))     # False
print(Node.is_valid_cpu("high"))  # False