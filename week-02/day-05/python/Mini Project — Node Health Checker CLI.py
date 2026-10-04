import argparse
import os
import sys

NODES = [
    {"id": "node-1", "status": "active", "cpu_usage": 45},
    {"id": "node-2", "status": "inactive", "cpu_usage": 0},
    {"id": "node-3", "status": "active", "cpu_usage": 88},
    {"id": "node-4", "status": "active", "cpu_usage": 92},
]


def require_env(var_name, default=None):
    value = os.getenv(var_name, default)
    if value is None:
        print(f"❌ Error: required environment variable '{var_name}' is not set.")
        sys.exit(1)
    return value


def check_nodes(threshold, verbose):
    region = require_env("CLOUD_REGION", default="eu-west-1")
    print(f"🌍 Checking nodes in region: {region}")
    print(f"⚙️  CPU threshold: {threshold}%\n")

    for node in NODES:
        if node["status"] != "active":
            if verbose:
                print(f"⏭️  {node['id']}: skipped (inactive)")
            continue

        if node["cpu_usage"] > threshold:
            print(f"🚨 {node['id']}: HIGH LOAD ({node['cpu_usage']}%)")
        elif verbose:
            print(f"✅ {node['id']}: OK ({node['cpu_usage']}%)")


def main():
    parser = argparse.ArgumentParser(description="Check node CPU health")
    parser.add_argument("--threshold", type=int, default=80, help="CPU usage threshold")
    parser.add_argument("--verbose", action="store_true", help="Show all nodes, not just high load")
    args = parser.parse_args()

    check_nodes(threshold=args.threshold, verbose=args.verbose)


if __name__ == "__main__":
    main()