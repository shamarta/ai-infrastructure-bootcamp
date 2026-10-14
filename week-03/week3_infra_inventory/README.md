# Infra Inventory

A small, tested Python toolkit for modeling cloud infrastructure nodes as objects, loading them from JSON, and reporting on their health. Built as the Week 3 capstone of an AI Infrastructure & Cloud Engineering bootcamp.

## Features
- Validated node models (`Node`, `ComputeNode`, `StorageNode`) built with dataclasses
- A factory (`node_from_dict`) that picks the right class from a `"type"` field
- An abstract `CloudProvider` interface with Azure and AWS implementations
- An `Inventory` that loads JSON, **skips and reports invalid records instead of crashing**, and answers questions (active nodes, overloaded nodes, average CPU, counts by type)
- A CLI with `--file` and `--threshold`

## Architecture
```
 JSON text ──► Inventory.from_json ──► node_from_dict ──► Node / ComputeNode / StorageNode
                    │                                            ▲
                    │ errors collected per bad record            │ validated in __post_init__
                    ▼
               print_report (cli.py)

 CloudProvider (ABC) ◄── AzureProvider, AWSProvider ──► Inventory.provision_via
```

## Project layout
```
src/infra_inventory/   models.py · providers.py · inventory.py · cli.py
tests/                 test_models.py · test_providers.py · test_inventory.py · test_cli.py
Dockerfile · pytest.ini · requirements.txt
```
CI lives in the repository root: `.github/workflows/week3-infra-inventory.yml`.

## Installation
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
PYTHONPATH=src python -m infra_inventory.cli                    # built-in demo data
PYTHONPATH=src python -m infra_inventory.cli --file nodes.json  # your own data
PYTHONPATH=src python -m infra_inventory.cli --threshold 70     # custom overload threshold
```

Input format — a JSON array of records:
```json
[{"id": "node-1", "type": "compute", "status": "active", "cpu_usage": 45, "cpu_cores": 8, "memory_gb": 32}]
```

Example output (demo data contains two deliberately invalid records):
```
📦 Inventory: demo-inventory
🖥️  Total nodes: 3
📊 By type: {'ComputeNode': 2, 'StorageNode': 1}
✅ Active nodes: 2
📈 Average active CPU: 66.5%
🚨 Overloaded (>80%): ['node-3']
⚠️  Skipped 2 invalid record(s):
   - record 3: cpu_usage must be between 0 and 100, got 150
   - record 4: unknown node type: 'gpu'
```

## Testing
```bash
python -m pytest -v
```

## Docker
```bash
docker build -t infra-inventory .
docker run --rm infra-inventory
```
The image runs as a non-root user.

## Design decisions
- **Validate at the boundary.** A `Node` cannot exist in an invalid state: `__post_init__` rejects bad status and out-of-range CPU. Bad data is caught when loaded, not later when it causes a confusing error.
- **Collect errors, don't crash.** One bad record in a feed shouldn't discard the rest, so `Inventory.from_json` records the problem and continues. Malformed JSON (not just one bad record) is still a hard error.
- **Program against an interface.** `Inventory.provision_via` accepts any `CloudProvider`; an incomplete provider can't even be instantiated.
- **`None` over `0` for "no data".** An average over zero active nodes is `None`, not `0%`.

## Security considerations
- Input is parsed with `json.loads` (no `eval`/`pickle`), and all fields are validated before use.
- The container runs as an unprivileged user and has no network or secret requirements.
- Providers here are simulated; real credentials would come from environment variables or a secret manager, never from source or JSON input.

## Limitations
- Cloud providers are mocks; no real API calls are made.
- Status changes after construction (e.g. in `decommission`) are not re-validated.

## Lessons learned
- Dataclass validation plus a type-dispatching factory removed most of the defensive `if "key" in dict` code I wrote with plain dictionaries.
- GitHub Actions only reads workflows from the repository **root**; a workflow inside a project subfolder never runs.