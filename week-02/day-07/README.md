# Week 2 — Day 7: Weekly Review & Combined Challenge

## 🎯 Goal
Consolidate everything learned in Week 2 (Days 1–6): string manipulation, nested data/JSON, exception handling, file I/O, CLI arguments/environment variables, and HTTP requests — by combining them into a single realistic function.

## 📚 Topics Reviewed
- String methods, slicing, and log-line parsing (Day 1)
- Nested data structures and `json.loads()`/`json.dumps()` (Day 2)
- `try`/`except`, multiple exception types, custom exceptions (Day 3)
- File reading/writing/appending, `json.dump()`/`json.load()` (Day 4)
- `argparse` and environment variables (Day 5)
- The `requests` library, status codes, and network error handling (Day 6)

## 💻 Combined Challenge — `fetch_and_save_report(url, filename)`
Built a function that:
1. Sends a GET request and catches all network/HTTP errors with `requests.exceptions.RequestException`
2. Parses the JSON response and writes it to a file with `json.dump()`, catching `ValueError` (invalid JSON) and `OSError` (file write failure) separately
3. Returns `True` on success and `False` on any failure, printing a clear message in each case — never letting an unhandled exception crash the script

## 🧠 Key Takeaways
- `requests.exceptions.RequestException` is the parent class of `Timeout`, `ConnectionError`, and `HTTPError` — catching it is a convenient way to handle "any request-related failure" in one place when a single error message is enough.
- A robust real-world function usually has multiple independent failure points (network, parsing, file I/O) that deserve separate `try`/`except` blocks, each with its own clear error message.
- Returning a boolean success/failure signal (rather than raising) lets the caller decide what to do next — a pattern used throughout this week (`safe_divide`, `safe_int`, `parse_node_line_safe`, and now `fetch_and_save_report`).

## ✅ Status
- [x] Knowledge test completed
- [x] Combined coding challenge completed
- [x] English review completed
- [x] Code committed and pushed to GitHub

## 📌 Week 2 Wrap-Up
All 7 days complete: strings/log parsing, nested data/JSON, exceptions, file handling, CLI args/env vars, API requests, and this combined review. Next: the Week 2 capstone project, following the production-readiness checklist established at the end of Week 1 (CI/CD, modular `src/`, `tests/`, `Dockerfile`, professional `README.md`).