class Node:
    def __init__(self, node_id, status):
        self.id = node_id
        self.status = status


class ComputeNode(Node):
    def __init__(self, node_id, status, cpu_cores):
        super().__init__(node_id, status)   # اول مقداردهی‌های کلاس پدر رو اجرا کن
        self.cpu_cores = cpu_cores           # بعد ویژگی‌های اختصاصی خودت رو اضافه کن


node = ComputeNode("node-1", "active", cpu_cores=8)
print(node.id, node.status, node.cpu_cores)