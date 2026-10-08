import json


class Node:
    total_created = 0

    def __init__(self, node_id, status, cpu_usage):
        if not Node.is_valid_cpu(cpu_usage):
            raise ValueError(f"Invalid cpu_usage for {node_id}: {cpu_usage}")
        self.id = node_id
        self.status = status
        self.cpu_usage = cpu_usage
        Node.total_created += 1

    @staticmethod
    def is_valid_cpu(value):
        return isinstance(value, (int, float)) and 0 <= value <= 100

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["status"], data["cpu_usage"])

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(",")
        return cls(parts[0], parts[1], int(parts[2]))

    @classmethod
    def from_json(cls, json_string):
        return cls.from_dict(json.loads(json_string))

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.cpu_usage < other.cpu_usage

    def __repr__(self):
        return f"Node({self.id}, {self.status}, {self.cpu_usage}%)"


def load_nodes():
    nodes = []

    # Source 1: a dictionary (like an API response item)
    nodes.append(Node.from_dict({"id": "node-1", "status": "active", "cpu_usage": 45}))

    # Source 2: a CSV-style line (like a flat file row)
    nodes.append(Node.from_csv_line("node-2,inactive,0"))

    # Source 3: a raw JSON string (like a raw HTTP response body)
    nodes.append(Node.from_json('{"id": "node-3", "status": "active", "cpu_usage": 88}'))

    # A source with bad data — should be rejected gracefully
    try:
        nodes.append(Node.from_csv_line("node-4,active,150"))
    except ValueError as e:
        print(f"⚠️  Skipped invalid node: {e}")

    return nodes


if __name__ == "__main__":
    nodes = load_nodes()

    print(f"\n✅ Nodes created: {Node.total_created}")
    print("📋 Sorted by CPU usage (lowest first):")
    for node in sorted(nodes):
        print(f"   - {node}")