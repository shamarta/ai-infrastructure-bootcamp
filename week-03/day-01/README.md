# Week 3 — Day 1: Object-Oriented Programming Basics (Classes & Objects)

## 🎯 Goal
Move from passing dictionaries around to modeling real things (servers, clusters) as classes with their own data and behavior, using `__init__`, methods, and `__str__`.

## 📚 Topics Covered
- Defining a class with `__init__` and `self`
- Instance attributes vs. methods
- `__str__` for readable object printing
- One class containing a list of instances of another class (`Cluster` containing `Node` objects)
- Methods that call other objects' methods (`cluster.overloaded_nodes()` calling `node.is_overloaded()`)

## 💻 Exercises
1. **Define a Basic Class** — `Node` with `__init__` storing `id`, `status`, `cpu_usage`
2. **Add a Method** — `is_overloaded(threshold)` using the object's own attributes
3. **String Representation with `__str__`** — readable `print(node)` output
4. **A Second Class That Contains a List of the First** — `Cluster` holding a list of `Node` objects, with `add_node()` and `active_node_count()`
5. **Class Method That Uses Another Object's Method** — `Cluster.overloaded_nodes()` calling each node's `is_overloaded()`

## 🛠 Mini Project — Cluster Management System
Built full `Node` and `Cluster` classes combining all of today's methods, plus `average_cpu_usage()` and a `print_report()` method that prints a complete cluster health summary, including the list of overloaded nodes using each node's `__str__`.

## 🧠 Key Takeaways
- A class bundles data (attributes) and behavior (methods) together — instead of a dictionary plus separate functions that operate on it, a `Node` object knows how to check if it's overloaded and how to describe itself.
- `self` always refers to the specific instance the method was called on — it's how an object accesses its own data.
- Objects can contain other objects (a `Cluster` holding a list of `Node`s), and methods on the outer object can call methods on the inner objects — this is how most real-world OOP code is structured.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Cluster Management System) completed
- [x] Code committed and pushed to GitHub