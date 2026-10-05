


def print_all_summaries(node_list):
    for node in node_list:
      
        print(f"[{node.__class__.__name__}] {node.id}: {node.resource_summary()}")


nodes = []
print_all_summaries(nodes)