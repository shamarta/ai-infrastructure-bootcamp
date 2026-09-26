# Week 2 — Day 4: File Handling for Config & Log Files

## 🎯 Goal
Learn to read, write, and append to files using context managers (`with`), and read/write structured config data using JSON files, applied to log-processing and configuration use cases.

## 📚 Topics Covered
- `open()` modes: `"w"` (write/overwrite), `"a"` (append), `"r"` (read)
- Context managers (`with open(...) as f:`) for automatic file closing
- Reading a file line by line and iterating over it
- `json.dump()` / `json.load()` for writing and reading structured config files
- Handling `FileNotFoundError` gracefully instead of crashing

## 💻 Exercises
1. **Write and Read a Text File** — `write_log`/`read_log` using `with open(..., "w"/"r")`
2. **Append to a Log File** — `append_log` using `"a"` mode to add without overwriting
3. **Read a File Line by Line** — `read_lines` returns a cleaned list of lines
4. **Write and Read JSON to/from a File** — `save_config`/`load_config` using `json.dump()`/`json.load()`
5. **Safe File Reading** — `safe_read_file` catches `FileNotFoundError` and returns `None`

## 🛠 Mini Project — Log File Analyzer
Wrote a sample multi-line log file, read it back, parsed each line with `parse_log_line` (from Day 1), and reported all `ERROR`-level lines plus a total/error line count — handling a missing file gracefully.

## 🧠



