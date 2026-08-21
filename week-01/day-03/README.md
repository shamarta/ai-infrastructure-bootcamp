# Day 03 — Python Conditions

## 🎯 Objective

Learn how to make Python programs make decisions based on different conditions.

By the end of this day, I can use conditional logic to control how a program behaves.

## Topics Covered

* `if`
* `if / else`
* `if / elif / else`
* Comparison operators

  * `==`
  * `!=`
  * `>`
  * `<`
  * `>=`
  * `<=`
* Logical operators

  * `and`
  * `or`
  * `not`
* Boolean values
* Nested conditions
* Indentation in Python

## 🧠 Key Concepts

Python uses indentation as part of its syntax.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Multiple conditions can be combined:

```python
if age >= 18 and is_verified and not is_banned:
    print("Access granted")
```

## 🧪 Exercises

### 1. Positive / Negative / Zero

Check whether a number is positive, negative, or zero.

### 2. Age Category

Classify users into:

* Child
* Teenager
* Adult
* Senior

### 3. Compare Numbers

Compare two numbers and determine which one is greater or whether they are equal.

### 4. Login System

Validate a username and password using conditional logic.

### 5. Access Control

Grant or deny access based on:

* Age
* Verification status
* Ban status

### 6. Mini Authentication System

A small authentication system that checks:

* Username
* Password
* User role

Supported roles:

* Admin
* User
* Guest

## 🚀 What I Learned

* How Python makes decisions using conditions
* How to compare values
* How to combine multiple conditions with logical operators
* How Boolean values work with conditions
* How to build a basic authentication and access-control system
* Why proper indentation is important in Python

## 📁 Project Structure

```text
day-03/
├── README.md
└── python/
    ├── 01_positive_negative_zero.py
    ├── 02_age_category.py
    ├── 03_compare_numbers.py
    ├── 04_login.py
    ├── 05_access_control.py
    └── 06_mini_authentication.py
```

## 🛠️ Environment

* Python 3
* Ubuntu on WSL2
* VS Code
* Git
* GitHub
