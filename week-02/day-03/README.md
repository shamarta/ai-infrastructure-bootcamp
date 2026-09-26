# Week 2 — Day 3: Exception Handling for Robust Infrastructure Scripts

## 🎯 Goal
Learn to handle errors gracefully with `try`/`except` instead of letting scripts crash on bad input, understand common exception types (`KeyError`, `ValueError`, `IndexError`, `ZeroDivisionError`), and build a custom exception for domain-specific validation.

## 📚 Topics Covered
- `try`/`except` basics and why exception handling matters for production scripts
- Handling multiple exception types separately, or together in one `except (TypeA, TypeB)` clause
- `else` (runs only if no exception occurred) and `finally` (always runs)
- Creating a custom exception class by subclassing `Exception`
- `raise` vs `return None`: when to stop execution vs. signal failure with a value

## 💻 Exercises
1. **Safe Division** — `safe_divide(a, b)` catches `ZeroDivisionError` and returns an error message instead of crashing
2. **Safe Integer Conversion** — `safe_int(value)` catches `ValueError` and returns `None` for non-numeric input
3. **Safe Dictionary Access** — `get_node_field(node, field)` catches `KeyError` and returns a readable "field not found" message
4. **Parse Node Line Safely** — `parse_node_line_safe(line)` catches both `IndexError` and `ValueError` together, returning `None` for malformed CSV-style lines
5. **Custom Exception for Node Validation** — `InvalidNodeDataError` (subclassing `Exception`) and `validate_node(node)`, which raises it when a required field is missing

## 🛠 Mini Project — Resilient Node Data Loader
Built `load_nodes(raw_nodes)`, which validates a list of node dictionaries (some intentionally malformed — missing fields or non-numeric `cpu_usage`), skips invalid entries with a warning instead of crashing, and reports how many nodes loaded successfully vs. were skipped.

## 🧠 Key Takeaways
- Real-world data is never guaranteed to be clean — scripts that process external data (API responses, user input, log files) need to handle malformed input without crashing.
- Different exception types should generally be handled separately so the specific cause of failure is clear, though closely related failures (like `IndexError` and `ValueError` from the same parsing step) can share one `except` clause.
- A custom exception (like `InvalidNodeDataError`) makes error handling self-documenting — anyone reading the code immediately understands what went wrong, rather than seeing a generic `Exception`.
- `raise` stops execution and forces the caller to handle the problem; returning `None` (or a sentinel value) lets the caller decide whether to treat the failure as fatal.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Resilient Node Data Loader) completed
- [x] Code committed and pushed to GitHub