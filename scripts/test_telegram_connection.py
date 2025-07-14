import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# Load credentials from .env
load_dotenv()
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

# Use a test session name
session_name = "test_session"

with TelegramClient(session_name, api_id, api_hash) as client:
    me = client.get_me()
    print("Connected successfully!")
    print(f"Name: {me.first_name} {me.last_name or ''}")
    print(f"Username: @{me.username}")
    print(f"User ID: {me.id}")
