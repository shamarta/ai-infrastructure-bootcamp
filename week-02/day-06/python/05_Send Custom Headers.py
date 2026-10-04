import requests

def get_with_auth(url, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.status_code, response.headers.get("Content-Type")

status, content_type = get_with_auth(
    "https://jsonplaceholder.typicode.com/users/1",
    token="fake-demo-token-123"
)
print(f"Status: {status}, Content-Type: {content_type}")