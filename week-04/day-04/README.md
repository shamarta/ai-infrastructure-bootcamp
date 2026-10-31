# Week 4 — Day 4: Comprehensions

## Learning Goals

- Create lists with list comprehensions.
- Filter values with conditional comprehensions.
- Transform records and build dictionaries with comprehensions.
- Use nested comprehensions and generator expressions for concise data processing.
- Combine these techniques in an infrastructure inventory report.

## Topics

- List comprehensions: `[expression for item in iterable]`
- Filtering with `if` in a comprehension
- Dictionary comprehensions: `{key: value for item in iterable}`
- Nested comprehensions for grouped data
- Generator expressions for memory-friendly aggregation

## Exercises

1. `exercise_01_node_names.py` — Extract node names with a list comprehension.
2. `exercise_02_filter_nodes.py` — Select nodes above a configurable CPU threshold.
3. `exercise_03_format_inventory.py` — Transform node records into readable lines.
4. `exercise_04_node_statuses.py` — Build a node-to-status dictionary.
5. `exercise_05_group_nodes_by_environment.py` — Group nodes by environment with a nested comprehension.

The shared functions are in `infrastructure_inventory.py`, and their automated tests are in
`test_infrastructure_inventory.py`.

## Mini Project: Infrastructure Inventory Report

`infrastructure_inventory.py` builds a report for an inventory of nodes. It summarizes
the number of nodes, average CPU and memory usage, and nodes that exceed configurable
resource thresholds. The report also includes each node's environment and status.

## Run the Exercises

Run these commands from this directory:

```bash
python exercise_01_node_names.py
python exercise_02_filter_nodes.py
python exercise_03_format_inventory.py
python exercise_04_node_statuses.py
python exercise_05_group_nodes_by_environment.py
```

Run the mini project:

```bash
python infrastructure_inventory.py
```

Run the tests:

```bash
python -m pytest -q
```
