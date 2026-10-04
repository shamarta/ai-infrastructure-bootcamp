# Week 2 — Day 6: Calling APIs with the `requests` Library

## 🎯 Goal
Learn to make real HTTP requests from Python using the `requests` library: sending GET requests, reading JSON responses, checking status codes, sending query parameters and headers, and handling network/HTTP errors gracefully.

## 📚 Topics Covered
- Basic GET requests with `requests.get()` and `.json()`
- Checking `response.status_code` before trusting response data
- Sending query parameters with the `params` argument
- Handling `Timeout`, `ConnectionError`, and `HTTPError` with `try`/`except`
- `response.raise_for_status()` to convert bad status codes into exceptions
- Sending custom headers (e.g. `Authorization: Bearer <token>`)

## 💻 Exercises
1. **Basic GET Request** — fetched a list of users from a public test API
2. **Check the Status Code Before Trusting the Response** — `get_user_safe()` returns `None` on a non-200 response instead of assuming success
3. **Send Query Parameters** — used `params={"userId": user_id}` instead of manually building the URL string
4. **Handle Network Errors Gracefully** — `safe_get()` catches `Timeout`, `ConnectionError`, and `HTTPError` separately
5. **Send Custom Headers** — sent an `Authorization: Bearer <token>` header, the standard pattern for authenticated APIs

## 🛠 Mini Project — Simple API Health Dashboard
Built a small dashboard that checks multiple API endpoints (including a deliberately broken one), reports UP/DOWN status, HTTP status code, and response time in milliseconds for each — a simplified version of a real uptime monitoring tool.

## 🧠 Key Takeaways
- A response with any status code (including 404 or 500) is still a "successful" HTTP call from `requests`' point of view — status codes must be checked explicitly, or `raise_for_status()` used to convert bad ones into exceptions.
- Network failures (timeout, no connection) are a different category of problem from HTTP errors (4xx/5xx) and are worth catching separately since they usually call for different handling.
- Query parameters and headers should be passed as dictionaries (`params=`, `headers=`) rather than manually concatenated into the URL string — this avoids encoding bugs and keeps code readable.

## ✅ Status
- [x] Theory completed
- [x] All 5 exercises completed
- [x] Mini-project (Simple API Health Dashboard) completed
- [x] Code committed and pushed to GitHub