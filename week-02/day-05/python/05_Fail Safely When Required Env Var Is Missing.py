import os
import sys

def require_env(var_name):
    value = os.getenv(var_name)
    if value is None:
        print(f"❌ Error: required environment variable '{var_name}' is not set.")
        sys.exit(1)  # خروج از برنامه با کد خطا (نه یک Exception خام)
    return value

api_key = require_env("API_KEY")
print(f"✅ API key loaded (length: {len(api_key)})")