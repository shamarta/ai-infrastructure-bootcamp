import json
import requests


def fetch_and_save_report(url, filename, timeout=5):
    # Step 1: make the request and handle network/HTTP errors
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Network/HTTP error: {e}")
        return False

    # Step 2: parse the JSON and save it to a file
    try:
        data = response.json()
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except (ValueError, OSError) as e:
        print(f"❌ Failed to save report: {e}")
        return False

    # Step 3: success
    print(f"✅ Report saved to {filename}")
    return True


if __name__ == "__main__":
    # Successful case
    fetch_and_save_report("https://jsonplaceholder.typicode.com/users", "users_report.json")

    # Failing case: bad URL (404)
    fetch_and_save_report("https://jsonplaceholder.typicode.com/nonexistent", "bad_report.json")

    # Failing case: unreachable host
    fetch_and_save_report("https://this-domain-does-not-exist-12345.com", "unreachable_report.json")