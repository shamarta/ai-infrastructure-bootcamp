# Week 1 — Day 6: Data Structures & Comprehensions in Infrastructure

## 🎯 Goal
Understand the differences between `list`, `tuple`, `dict`, and `set`; grasp the mutable vs immutable distinction; understand why `set` lookups are faster than `list` lookups; and use list/dictionary/set comprehensions to process infrastructure-style data (a list of node dictionaries similar to a cloud API response).

## 📚 Topics Covered
- `list` vs `tuple` — mutability and when to use each
- `dict` — key-value structure used by JSON/YAML and cloud API responses
- `set` — unique, unordered collection with O(1) average lookup time
- List comprehensions and set comprehensions for filtering/mapping data
- Dictionary comprehensions for building key-value maps from data
- Time complexity intuition: O(n) list search vs O(1) set search

## 💻 Exercises
1. Filter Numbers Greater Than 10 Using List Comprehension
2. Tuple Immutability Test — confirmed tuples raise `TypeError: 'tuple' object does not support item assignment` when modification is attempted
3. `get_inactive_node_ids(nodes)` — returns ids of inactive nodes
4. `has_duplicate_ips(nodes)` — detects duplicate IPs by comparing list length to set length
5. `average_cpu_usage(nodes)` — returns average CPU usage of active nodes only (returns `None`, not `0`, when there's no data to average)
6. `get_active_cpu_map(nodes)` — dictionary comprehension building `{node_id: cpu_usage}` for active nodes

## 🛠 Mini Project — Cloud Node Monitor
Built `node_monitor.py`, combining all of today's functions into a single report generator (`print_report`) that prints:
- Unique active IPs
- High-load nodes (CPU usage above threshold)
- Inactive node ids
- A duplicate-IP warning
- Average active CPU usage
- A map of active node ids to their CPU usage

## 🧠 Key Takeaways
- Tuples are immutable — useful for values that should never change, like a fixed server address or config constant.
- Sets provide near-constant-time (O(1)) membership checks, making them ideal for deduplicating IPs or log entries at scale.
- Comprehensions are a concise, often faster alternative to writing out full `for` loops when building a new list, set, or dictionary.
- Returning `None` instead of `0` for "no data" cases avoids conflating "no active nodes" with "zero average load" — an important distinction in real monitoring systems.

## ✅ Status
- [x] Theory completed
- [x] All 6 exercises completed
- [x] Mini-project (Cloud Node Monitor) completed
- [x] Code committed and pushed to GitHub