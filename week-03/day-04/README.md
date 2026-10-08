# Week 3 — Day 4: Class Methods, Static Methods & Dunder Methods

## 🎯 Goal
Learn to build objects from different data sources using alternative constructors (`@classmethod`), organize helper logic inside a class (`@staticmethod`), share state across instances (class attributes), and customize how objects behave with Python's built-in operators (`__eq__`, `__lt__`, `__repr__`).

## 📚 Topics Covered
- Class attributes (shared across all instances) vs. instance attributes
- `@classmethod` with `cls` for alternative constructors (`from_dict`, `from_csv_line`, `from_json`)
- `@staticmethod` for helper functions that logically belong to a class but don't need `self` or `cls`
- Dunder methods: `__eq__` (equality), `__lt__` (ordering, enabling `sorted()`), `__repr__` (developer-friendly representation)

## 💻 Exercises
1. **Class Attribute** — `Node.total_created` counts instances across all objects
2. **Alternative Constructor with `@classmethod`** — `Node.from_dict(data)`
3. **Alternative Constructor from a CSV-Style Line** — `Node.from_csv_line(line)`
4. **Static Method** — `Node.is_valid_cpu(value)` validation helper
5. **Dunder Methods** — `__eq__`, `__lt__`, `__repr__` enabling `==`, `<`, and `sorted()` on `Node` objects

## 🛠 Mini Project — Node Loader from Multiple Sources
Built a `Node` class that can be constructed from a dictionary, a CSV line, or a raw JSON string (all via `@classmethod`s), validates `cpu_usage` with a `@staticmethod` before creating the object, rejects invalid input with a clear error, tracks total instances with a class attribute, and supports sorting by CPU usage through `__lt__`.

## 🧠 Key Takeaways
- Alternative constructors (`@classmethod`) are the standard Python way to build objects from different input formats without cluttering `__init__` with conditional logic.
- A `@staticmethod` is just a regular function that's organized inside a class for clarity; it can't access instance or class state.
- Defining `__lt__` is enough to make `sorted()` work on a list of custom objects, with no need for a separate `key=` function.
- Class attributes are shared state — modifying one affects every instance, so they should be used deliberately (e.g., counters), not as a substitute for instance attributes.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Node Loader from Multiple Sources) completed
- [x] Code committed and pushed to GitHub