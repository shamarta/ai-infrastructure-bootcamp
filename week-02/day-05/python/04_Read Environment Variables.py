import os

def get_config():
    region = os.getenv("CLOUD_REGION", "eu-west-1")  # مقدار پیش‌فرض اگه ست نشده باشه
    api_key = os.getenv("API_KEY")  # بدون پیش‌فرض؛ اگه نباشه None برمی‌گرده

    return region, api_key

region, api_key = get_config()
print(f"Region: {region}")
print(f"API Key set: {api_key is not None}")