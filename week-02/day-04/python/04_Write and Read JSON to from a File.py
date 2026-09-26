import json

def save_config(filename, config):
    with open(filename, "w") as f:
        json.dump(config, f, indent=2)


def load_config(filename):
    with open(filename, "r") as f:
        return json.load(f)


config = {"region": "eu-west-1", "provider": "azure", "max_nodes": 10}
save_config("config.json", config)
print(load_config("config.json"))