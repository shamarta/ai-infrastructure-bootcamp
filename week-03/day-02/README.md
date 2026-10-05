# Week 3 — Day 2: Inheritance & Polymorphism

## 🎯 Goal
Learn to build specialized classes from a shared base class using inheritance, override behavior in subclasses, and use polymorphism to treat different node types uniformly through a shared interface.

## 📚 Topics Covered
- Inheritance: `class ComputeNode(Node):` inherits attributes and methods from `Node`
- `super().__init__(...)` to extend (not replace) the parent class's initialization
- Overriding a method in a subclass to give it specialized behavior
- Polymorphism: calling the same method name (`resource_summary()`) on different object types and getting type-specific results, without checking the type explicitly
- `self.__class__.__name__` to get an object's actual class name at runtime

## 💻 Exercises
1. **Basic Inheritance** — `ComputeNode(Node)` with no changes, confirming `isinstance()` still works
2. **Extend `__init__` with `super()`** — `ComputeNode` adds `cpu_cores` while reusing `Node`'s setup via `super()`
3. **Override a Method** — `StorageNode.describe()` completely replaces the parent's version
4. **Two Different Subclasses with Different Behavior** — `ComputeNode` and `StorageNode` each implement `resource_summary()` differently
5. **Polymorphism in a Loop** — iterating over mixed node types and calling `resource_summary()` on each without checking type

## 🛠 Mini Project — Heterogeneous Cluster Report
Built a `Cluster` that holds a mix of `ComputeNode` and `StorageNode` objects, counts nodes by type, and prints a unified report calling each node's own `resource_summary()` — demonstrating polymorphism in a realistic infrastructure context.

## 🧠 Key Takeaways
- Inheritance avoids duplicating code across similar classes — shared setup and behavior live in the base class (`Node`), while subclasses add or override only what's different.
- `super().__init__(...)` should generally be called first in a subclass's `__init__` so the parent's setup runs before subclass-specific attributes are added.
- Polymorphism means calling code (like `print_all_summaries` or `Cluster.print_report`) doesn't need to know or check which subclass it's dealing with — it just calls the shared method name and each object responds in its own way.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Heterogeneous Cluster Report) completed
- [x] Code committed and pushed to GitHub