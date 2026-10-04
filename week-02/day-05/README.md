# Week 2 — Day 5: CLI Arguments & Environment Variables

## 🎯 Goal
Turn Python scripts into real CLI tools by reading command-line arguments (`sys.argv`, `argparse`) and environment variables (`os.getenv`), the way infrastructure tools like `kubectl` or `terraform` are configured.

## 📚 Topics Covered
- Reading raw command-line arguments with `sys.argv`
- Named arguments and auto-generated help text with `argparse`
- Boolean flags with `action="store_true"`
- Reading environment variables with `os.getenv()`, with and without defaults
- Failing safely (`sys.exit(1)`) with a clear message when a required environment variable is missing

## 💻 Exercises
1. **Basic CLI Arguments with sys.argv** — reads raw positional arguments from the command line
2. **Parse Named Arguments with argparse** — `--node-id` and `--threshold` flags with types and defaults
3. **Optional Flags (Boolean Arguments)** — a `--dry-run` flag using `action="store_true"`
4. **Read Environment Variables** — `os.getenv()` with a default value vs. no default
5. **Fail Safely When Required Env Var Is Missing** — `require_env()` exits with a clear error instead of crashing with a raw exception

## 🛠 Mini Project — Node Health Checker CLI
Built `node_health_checker.py`, a CLI tool that accepts `--threshold` and `--verbose` flags, reads the deployment region from an environment variable (with a default), and reports which active nodes exceed the CPU threshold.

## 🧠 Key Takeaways
- `argparse` is the standard way to build real CLI tools in Python — it gives named arguments, type checking, defaults, and free `--help` output.
- Environment variables are the standard way to pass configuration (especially secrets like API keys) into a script without hardcoding them or exposing them in command history.
- Failing with `sys.exit(1)` and a clear message is far more usable than letting a script crash with a raw traceback when required configuration is missing.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Node Health Checker CLI) completed
- [x] Code committed and pushed to GitHub