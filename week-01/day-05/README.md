# Week 1 — Day 5: Functions, Parameters & Scope

## 🎯 Goal
Learn how to write modular, reusable functions in Python using `def`, understand the difference between `return` and `print`, use default parameters, and understand variable scope (local vs global). Refactor the Number Guessing Game from Day 4 into a clean, function-based structure.

## 📚 Topics Covered
- Defining functions with `def`
- Parameters vs arguments
- `return` vs `print` — returning values vs displaying output
- Default parameter values
- Local vs global variable scope
- The `global` keyword and `UnboundLocalError`
- Basic type hints (`def func(x: int) -> int:`)

## 💻 Exercises
1. `square(n)` — returns the square of a number
2. `is_even(n)` — returns `True`/`False` for even numbers
3. `greet(name="friend")` — greeting function with a default parameter
4. `max_of_three(a, b, c)` — returns the largest of three numbers
5. `count_vowels(text)` — counts vowels in a string
6. Scope bug demo — reproducing and fixing an `UnboundLocalError` using `global`
7. `validate_password(password, min_length=8, max_length=20)` — validates password rules
8. `calculate_stats(numbers)` — returns a dictionary with `min`, `max`, and `average` of a list

## 🛠 Mini Project
Refactored the Day 4 Number Guessing Game into a function-based structure:
- `generate_secret_number()`
- `get_user_guess()`
- `check_guess(guess, secret)`
- `play_game()`

Each function follows the Single Responsibility Principle — one function, one clear job.

## 🧠 Key Takeaways
- `return` sends a value back to be used elsewhere in the program; `print` only displays it on screen.
- Assigning to a variable inside a function makes Python treat it as local — even if a global variable with the same name exists — unless you explicitly declare it with `global`.
- Splitting a program into small functions makes code easier to read, test, and reuse — a pattern used constantly in real-world engineering.

## ✅ Status
- [x] Theory completed
- [x] All exercises completed
- [x] Mini-project completed
- [x] Code committed and pushed to GitHub
- [x] Technical English reviewed