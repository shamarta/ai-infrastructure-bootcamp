# Week 3 — Day 6: Modules, Packages & Project Structure

## 🎯 Goal
Learn to split code across multiple files and folders, import between them correctly, and organize classes into a reusable package — the foundation of any real Python project (and of the `src/` layout used in production repositories).

## 📚 Topics Covered
- Modules: every `.py` file is a module; `import module` vs. `from module import name`
- The `if __name__ == "__main__":` guard to separate "run directly" code from "imported" code
- Packages: folders with `__init__.py` grouping related modules
- Re-exporting names in `__init__.py` to simplify a package's public interface
- Relative imports (`from .models import Node`) for modules inside the same package

## 💻 Exercises
1. **Import a Whole Module** — `import helpers` and calling `helpers.function()`
2. **Import Specific Names with `from ... import`** — shared `Node`/`Cluster` classes in `models.py`, imported by `main.py`
3. **The `if __name__ == "__main__":` Guard** — code that runs only on direct execution, not on import
4. **Create a Package** — an `infra/` package with `__init__.py` re-exporting `Node` and `print_report`
5. **Relative Imports Inside a Package** — `cluster.py` importing from `models.py` via `from .models import Node`

## 🛠 Mini Project — Infra Toolkit Package
Reorganized the week's `Node` (as a dataclass with validation and a computed `is_overloaded` property) and `Cluster` classes into a proper `infra_toolkit` package with `models.py`, `cluster.py`, and `cli.py`, plus a thin `run.py` entry point outside the package.

## 🧠 Key Takeaways
- Each Python file is isolated by default; sharing a class between files requires importing it, not copy-pasting its definition — this resolves the `NameError` encountered earlier when a class was defined in a different file.
- `__init__.py` can re-export names so users of a package write `from infra import Node` instead of `from infra.models import Node`, keeping the internal file layout an implementation detail.
- Relative imports (`.`) are the standard way for modules *inside* a package to refer to each other, while entry-point scripts outside the package use absolute imports.
- A thin entry-point script (`run.py`) that just calls a `main()` function inside the package is a common, clean pattern for CLI-style projects.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Infra Toolkit Package) completed
- [x] Code committed and pushed to GitHub