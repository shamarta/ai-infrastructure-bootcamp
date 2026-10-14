"""Command-line entry point: load an inventory and print a health report."""

from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from .inventory import Inventory

DEMO_JSON = """
[
  {"id": "node-1", "type": "compute", "status": "active", "cpu_usage": 45, "cpu_cores": 8, "memory_gb": 32},
  {"id": "node-2", "type": "storage", "status": "inactive", "cpu_usage": 0, "capacity_gb": 1000},
  {"id": "node-3", "type": "compute", "status": "active", "cpu_usage": 88, "cpu_cores": 16, "memory_gb": 64},
  {"id": "node-4", "type": "compute", "status": "active", "cpu_usage": 150},
  {"id": "node-5", "type": "gpu", "status": "active", "cpu_usage": 10}
]
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Infrastructure inventory health report")
    parser.add_argument("--file", help="path to a JSON file of node records (default: built-in demo data)")
    parser.add_argument("--threshold", type=float, default=80.0, help="CPU %% above which a node is overloaded")
    return parser


def print_report(inventory: Inventory, threshold: float) -> None:
    print(f"📦 Inventory: {inventory.name}")
    print(f"🖥️  Total nodes: {len(inventory)}")
    print(f"📊 By type: {inventory.count_by_type()}")
    print(f"✅ Active nodes: {len(inventory.active_nodes())}")

    average = inventory.average_cpu_usage()
    print(f"📈 Average active CPU: {average:.1f}%" if average is not None else "📈 Average active CPU: N/A")

    overloaded = [n.id for n in inventory.overloaded_nodes(threshold)]
    print(f"🚨 Overloaded (>{threshold:g}%): {overloaded}")

    if inventory.errors:
        print(f"⚠️  Skipped {len(inventory.errors)} invalid record(s):")
        for message in inventory.errors:
            print(f"   - {message}")


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError as exc:
            print(f"❌ Cannot read {args.file}: {exc}", file=sys.stderr)
            return 1
    else:
        text = DEMO_JSON

    try:
        inventory = Inventory.from_json("demo-inventory", text)
    except ValueError as exc:
        print(f"❌ Invalid JSON input: {exc}", file=sys.stderr)
        return 1

    print_report(inventory, args.threshold)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())