# Week 2 — Day 2: Nested Data Structures & JSON-like Parsing

## 🎯 Goal
Work with nested data structures (dictionaries inside lists, dictionaries inside dictionaries), the kind of structure returned by real cloud APIs, and learn to serialize/deserialize data with Python's `json` module.

## 📚 Topics Covered
- Nested dictionaries and lists, and why real cloud API responses are structured this way
- Deep/nested access with chained indexing (`cluster["nodes"][2]["tags"]["team"]`)
- Looping over nested structures
- `json.loads()` (deserialize: JSON string → Python dict) and `json.dumps()` (serialize: Python dict → JSON string), including `indent` for readable output
- The "group by key" pattern: checking whether a dictionary key exists before appending to it

## 💻 Exercises
1. **Get Region and Node Count** — printed `cluster["region"]` and `len(cluster["nodes"])`
2. **Access a Deeply Nested Value** — retrieved a specific node's team via chained indexing (`cluster["nodes"][2]["tags"]["team"]`)
3. **List All Production Node IDs** — list comprehension filtering nodes where `tags["env"] == "production"`
4. **Convert Cluster to JSON String** — used `json.dumps(cluster, indent=2)` to serialize the cluster dictionary
5. **Group Node IDs by Team** — `group_by_team(cluster)` builds `{team: [node_ids]}` by checking if a key exists before creating it

## 🛠 Mini Project — Cluster Report from JSON String
Built a script that takes a raw JSON string (simulating a real cloud API response), deserializes it with `json.loads()`, and prints a summary report: cluster name/provider/region, total node count, active node count, and nodes grouped by team (reusing `group_by_team`).

## 🧠 Key Takeaways
- Real cloud API responses are nested (dict → list → dict → dict) because they represent hierarchical resources (a cluster containing nodes, each with their own tags) — a flat structure couldn't represent that.
- `json.loads()` and `json.dumps()` are opposites: one turns a JSON string into a usable Python dict, the other turns a Python dict into a JSON string for transmission or storage.
- The "check if key exists, else create it, then append" pattern is the standard way to group items by a property when a comprehension alone isn't enough.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Cluster Report from JSON String) completed
- [x] Code committed and pushed to GitHub
