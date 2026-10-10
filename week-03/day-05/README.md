# Week 3 — Day 5: Dataclasses & Abstract Base Classes

## 🎯 Goal
Learn to model data-centric classes concisely with `@dataclass`, and define enforceable interfaces with Abstract Base Classes (ABC) so different implementations (e.g., cloud providers) can be used interchangeably.

## 📚 Topics Covered
- `@dataclass`: auto-generated `__init__`, `__repr__`, and `__eq__` from type-annotated fields
- Default values and `field(default_factory=...)` for mutable defaults like lists
- `frozen=True` for immutable dataclasses
- `__post_init__` for validation after a dataclass is constructed
- `ABC` and `@abstractmethod` to define an interface that subclasses must implement

## 💻 Exercises
1. **Basic Dataclass** — `Node` with auto-generated `__init__`/`__repr__`/`__eq__`
2. **Default Values and `field()`** — `Cluster` with a safe `default_factory=list`
3. **Frozen (Immutable) Dataclass** — `ServerAddress` that rejects attribute assignment
4. **Validation with `__post_init__`** — rejecting an out-of-range `cpu_usage` at construction time
5. **Abstract Base Class** — `CloudProvider` interface; incomplete subclasses fail at instantiation time

## 🛠 Mini Project — Multi-Cloud Provisioner
Defined a `CloudProvider` abstract interface with `AzureProvider` and `AWSProvider` implementations, modeled servers with a `Server` dataclass, and built a `Provisioner` that deploys and tears down servers through any provider without knowing which one it's using — combining dataclasses, ABCs, and polymorphism.

## 🧠 Key Takeaways
- `@dataclass` removes the boilerplate of data-holding classes, but mutable defaults (lists, dicts) must use `field(default_factory=...)` to avoid state being shared across instances.
- An ABC turns an informal convention ("every provider should have `create_server`") into something Python actively enforces — a subclass missing an abstract method can't even be instantiated.
- Programming against an interface (`CloudProvider`) instead of a concrete class (`AzureProvider`) is what makes code swappable and testable — the same idea underlies Terraform providers and most cloud SDK plugin systems.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Multi-Cloud Provisioner) completed
- [x] Code committed and pushed to GitHub