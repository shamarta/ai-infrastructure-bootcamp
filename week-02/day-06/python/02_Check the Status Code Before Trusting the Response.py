import requests

def get_user_safe(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

user = get_user_safe(1)
print(user["name"] if user else "No user found")

missing_user = get_user_safe(9999)
print(missing_user)