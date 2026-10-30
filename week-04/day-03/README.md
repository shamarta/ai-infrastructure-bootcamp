# Week 4 — Day 3: Higher-Order Functions

## Learning Goals

- Use `lambda` expressions for short, focused operations.
- Transform data with `map`.
- Select matching data with `filter`.
- Sort records with a `key` function.
- Combine these tools to analyze infrastructure node metrics.

## Exercises

1. `exercise_01_lambda_and_sorted.py` — Sort nodes using a lambda as the key.
2. `exercise_02_map_cpu_values.py` — Format CPU values with `map`.
3. `exercise_03_filter_overloaded_nodes.py` — Select overloaded nodes with `filter`.
4. `exercise_04_sort_nodes.py` — Sort node records in ascending and descending order.
5. `exercise_05_compose_node_metrics.py` — Compose transformations into a node report.

The shared functions are in `node_metrics.py`, and automated tests are in
`test_node_metrics.py`.

## Mini Project: Node Metrics Report

The mini project reports the cluster size, average CPU usage, and number of
overloaded nodes. It lists nodes from highest to lowest CPU usage and supports
a custom overload threshold.

## Run the Exercises

Run these commands from this directory:

```bash
python exercise_01_lambda_and_sorted.py
python exercise_02_map_cpu_values.py
python exercise_03_filter_overloaded_nodes.py
python exercise_04_sort_nodes.py
python exercise_05_compose_node_metrics.py
```

Run the mini project:

```bash
python node_metrics.py
```

Run the tests:

```bash
python -m pytest -q
```
