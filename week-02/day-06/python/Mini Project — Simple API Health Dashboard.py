import requests

ENDPOINTS = {
    "Users API": "https://jsonplaceholder.typicode.com/users",
    "Posts API": "https://jsonplaceholder.typicode.com/posts",
    "Broken API": "https://jsonplaceholder.typicode.com/nonexistent",
}


def check_endpoint(name, url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return {
            "name": name,
            "status": "✅ UP",
            "status_code": response.status_code,
            "response_time_ms": round(response.elapsed.total_seconds() * 1000, 1),
        }
    except requests.exceptions.Timeout:
        return {"name": name, "status": "❌ TIMEOUT", "status_code": None, "response_time_ms": None}
    except requests.exceptions.ConnectionError:
        return {"name": name, "status": "❌ CONNECTION ERROR", "status_code": None, "response_time_ms": None}
    except requests.exceptions.HTTPError:
        return {"name": name, "status": "❌ DOWN", "status_code": response.status_code, "response_time_ms": None}


def print_dashboard(endpoints):
    print("📊 API Health Dashboard\n" + "-" * 40)
    for name, url in endpoints.items():
        result = check_endpoint(name, url)
        print(f"{result['status']:<20} {result['name']:<15} "
              f"({result['status_code']}, {result['response_time_ms']} ms)")


if __name__ == "__main__":
    print_dashboard(ENDPOINTS)