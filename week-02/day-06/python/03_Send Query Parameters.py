import requests

def get_posts_by_user(user_id):
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": user_id}
    )
    return response.json()

posts = get_posts_by_user(1)
print(f"User 1 has {len(posts)} posts")