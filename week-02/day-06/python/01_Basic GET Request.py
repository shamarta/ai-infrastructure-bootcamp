import requests

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()

users = get_users()
print(f"Total users: {len(users)}")
print(users[0])