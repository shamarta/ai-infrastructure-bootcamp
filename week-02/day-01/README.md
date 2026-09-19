# Week 2 — Day 1: Strings in Depth (String Manipulation for Infrastructure & Logs)

## 🎯 Goal
Learn practical string manipulation in Python: common string methods, slicing, and f-string formatting, then apply them to parse realistic infrastructure/log-style text data.

## 📚 Topics Covered
- Core string methods: `.strip()`, `.lower()`, `.upper()`, `.startswith()`, `.replace()`
- Converting between strings and lists with `.split()` and `.join()`
- String slicing (`text[start:stop:step]`), including reversing a string with `text[::-1]`
- Advanced f-string formatting (decimal precision, padding)
- Parsing structured text (CSV-style lines and full log lines) into dictionaries

## 💻 Exercises
1. **Clean and Normalize a Log Line** — stripped whitespace and lowercased a raw log string
2. **Extract IP Octets** — `get_ip_octets(ip)` splits an IP address into its 4 parts
3. **Parse a CSV-style Line** — `parse_node_line(line)` converts a `"id,status,cpu_usage"` string into a dictionary, converting `cpu_usage` to an integer
4. **Reverse a String Using Slicing** — `reverse_string(text)` reverses a string with `text[::-1]`
5. **Parse a Full Log Line** — `parse_log_line(line)` parses a line like `"2024-06-01 14:32:10 [ERROR] node-3: Connection timeout after 30s"` into a dictionary with `date`, `time`, `level`, `node`, and `message`

## 🛠 Mini Project — Simple Log Line Parser
Built a script that parses a list of log lines using `parse_log_line()` and prints only the lines whose level is `ERROR`, in a readable format with a timestamp, node name, and message.

## 🧠 Key Takeaways
- `.split(sep, maxsplit)` with a limited `maxsplit` prevents breaking a message that itself contains the delimiter (e.g. splitting only the first `": "` to separate a node name from its message).
- Values extracted with `.split()` are always strings — numeric fields like `cpu_usage` must be explicitly converted with `int()`.
- Small parsing functions built earlier in the day can be reused directly in a larger script instead of being rewritten.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Simple Log Line Parser) completed
- [x] Code committed and pushed to GitHub