# Week 1 — Day 7: Weekly Review & Assessment

## 🎯 Goal
Consolidate everything learned in Week 1 (Days 1–6): Python fundamentals, control flow, functions, scope, and data structures/comprehensions. Confirm understanding through a knowledge test, a combined coding challenge, and an English review question before moving to Week 2.

## 📚 Topics Reviewed
- Variables, data types, strings, collections (Week 1 recap)
- Control flow: `if`/`elif`/`else`, loops, `break`/`continue`
- Functions: `def`, parameters vs arguments, `return` vs `print`, default parameters
- Scope: local vs global, `global` keyword, `UnboundLocalError`
- Data structures: `list`, `tuple`, `dict`, `set` — mutability and time complexity
- List/set/dictionary comprehensions
- Why `elif` can silently skip a check when conditions aren't mutually exclusive

## 💻 Exercises
1. **Build a Node Summary Dictionary** — `get_node_summary(nodes)` combines smaller functions (`get_unique_active_ips`, `average_cpu_usage`) into a single summary dict with total/active/inactive counts, unique IP count, and average active CPU usage.
2. **When `elif` Causes a Bug** — demonstrated how using `elif` instead of two independent `if` statements causes `is_upper` to be silently skipped for a character that is both alphabetic and uppercase, then fixed it with separate `if` statements.

## 🧠 Key Takeaways
- Small, single-purpose functions (like `average_cpu_usage`, `get_unique_active_ips`) can be composed into larger functions (`get_node_summary`) — a pattern used constantly in real engineering.
- `elif` should only be used when conditions are truly mutually exclusive. When conditions can both be true independently, separate `if` statements are required, or later checks get silently skipped.
- Returning `None` instead of `0` for "no data" cases remains an important distinction carried over from Day 6.

## ✅ Status
- [x] Knowledge test completed
- [x] Coding challenges completed
- [x] English review completed
- [x] Code committed and pushed to GitHub

## 📌 Program Update (effective this week)
Starting Week 1, Day 7, two standing additions were introduced to the 18-month program:
1. **Production-readiness checklist** for main/end-of-week projects: CI/CD pipeline, modular `src/` structure with type hints and docstrings, `tests/` with pytest, `Dockerfile`, and a professional `README.md` with architecture diagram and benchmarks.
2. **End-of-week technical article formula** for writing a Medium/Dev.to/LinkedIn post: problem-focused title, problem statement, architecture & solution, code & benchmarks, key takeaways.