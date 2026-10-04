import requests

def safe_get(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # اگه status code خطا بود (4xx/5xx)، Exception پرتاب می‌کنه
        return response.json()
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
        return None

data = safe_get("https://jsonplaceholder.typicode.com/users/1")
print(data)

bad_data = safe_get("https://jsonplaceholder.typicode.com/nonexistent")
print(bad_data)