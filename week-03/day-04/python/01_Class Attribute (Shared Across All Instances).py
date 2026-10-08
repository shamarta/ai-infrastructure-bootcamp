class Node:
    total_created = 0   # class attribute — مشترک بین همه‌ی nodeها

    def __init__(self, node_id):
        self.id = node_id
        Node.total_created += 1


n1 = Node("node-1")
n2 = Node("node-2")
n3 = Node("node-3")

print(Node.total_created)   # 3
print(n1.total_created)     # 3 (هم از طریق شیء هم از طریق خود کلاس قابل‌دسترسیه)