import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CONFIG = {
    "client_name": os.getenv("CLIENT_NAME"),
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "client_redirect": "http://127.0.0.1:8080/authorized",
    "server_base_url": "https://accounts.freelancer-sandbox.com",
}

# Optional: sanity check to avoid silent failures
for key, value in CONFIG.items():
    if value is None:
        print(f"⚠️ Warning: {key} is not set in your environment")
