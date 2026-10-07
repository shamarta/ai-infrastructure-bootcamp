# Week 3 — Day 3: Encapsulation & Properties

## 🎯 Goal
Learn to protect an object's internal data using encapsulation conventions (`_attribute`), and use `@property`/`@x.setter` to validate values on assignment and compute derived values on access — so an object can never be set into an invalid state.

## 📚 Topics Covered
- The single-underscore convention (`_cpu_usage`) for "internal use" attributes
- `@property` to expose a method as a read-only attribute-like value
- `@x.setter` to validate a value before it's stored, raising `TypeError`/`ValueError` on invalid input
- Computed properties (like `is_overloaded`) that derive their value from other attributes instead of storing their own
- Using `setattr()` to set an attribute dynamically by name, and catching validation errors from a property setter

## 💻 Exercises
1. **Private Attribute with a Single Underscore** — `_cpu_usage` as a convention-based internal attribute
2. **Read-Only Property** — `cpu_usage` exposed via `@property` with no setter, raising `AttributeError` on assignment
3. **Property with Validation (Setter)** — `@cpu_usage.setter` rejects non-numeric or out-of-range values
4. **Computed Property** — `is_healthy` recalculates from `status` and `cpu_usage` every time it's accessed
5. **Combine Validation Setter + Computed Property** — both patterns together on one `Node` class

## 🛠 Mini Project — Self-Validating Node Model
Built a `Node` class where both `status` and `cpu_usage` are validated properties (status restricted to a fixed set of valid values, cpu_usage restricted to 0–100 and numeric), plus a computed `is_overloaded` property. A `try_update()` helper attempts various valid and invalid updates and reports which succeeded or were rejected.

## 🧠 Key Takeaways
- A property setter is the single place where validation logic for an attribute lives — every assignment (from `__init__` or later code) goes through it, so an object can never silently hold an invalid value.
- A computed property (no setter, no stored value) is useful for values that should always reflect current state (like `is_overloaded`) rather than being manually kept in sync.
- Encapsulation in Python is convention-based (`_name`), not enforced like in some other languages — properties are the real mechanism for controlling how a value can be read or changed.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Self-Validating Node Model) completed
- [x] Code committed and pushed to GitHub