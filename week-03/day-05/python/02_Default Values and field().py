from dataclasses import dataclass, field
from typing import List


@dataclass
class Cluster:
    name: str
    region: str = "eu-west-1"                       # مقدار پیش‌فرض ساده
    nodes: List[str] = field(default_factory=list)  # لیست خالیِ جدید برای هر شیء


c1 = Cluster("prod-1")
c2 = Cluster("prod-2", region="us-east-1")

c1.nodes.append("node-1")
print(c1)   # Cluster(name='prod-1', region='eu-west-1', nodes=['node-1'])
print(c2)   # Cluster(name='prod-2', region='us-east-1', nodes=[])