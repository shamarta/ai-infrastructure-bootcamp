# Week 4 — Day 2: Function Scope and Composition

## Learning Goals

- Distinguish local variables from module-level names.
- Return locally-created data from a function.
- Use module-level constants without mutating global state.
- Pass configuration into functions as parameters.
- Compose small functions into a larger infrastructure report.

## Exercises

1. `exercise_01_local_scope.py` — Create and return a function-local value.
2. `exercise_02_module_constant.py` — Read a module-level constant in a function.
3. `exercise_03_local_data_and_return.py` — Build a local list and return it.
4. `exercise_04_parameter_over_global_state.py` — Override behavior with a parameter instead of changing global state.
5. `exercise_05_composing_functions.py` — Combine focused functions to build a cluster report.

## Mini Project: Cluster Health Report

`mini_project_cluster_report.py` creates a report for a list of infrastructure nodes. It shows the number of nodes, average CPU usage, and whether each node is normal or overloaded. The default overload threshold is 80%, and callers can supply a different threshold.

Run the mini project:

```bash
python mini_project_cluster_report.py
```

Run the exercises:

```bash
python exercise_01_local_scope.py
python exercise_02_module_constant.py
python exercise_03_local_data_and_return.py
python exercise_04_parameter_over_global_state.py
python exercise_05_composing_functions.py
```

Run the tests:

```bash
python -m pytest -q
```
