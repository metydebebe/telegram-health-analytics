import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto

# Load credentials
load_dotenv()
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

# Define channels
channels = {
    "lobelia4cosmetics": "https://t.me/lobelia4cosmetics",
    "tikvahpharma": "https://t.me/tikvahpharma",
    # Add more here as needed
}

# Setup output folders
today = datetime.today().strftime("%Y-%m-%d")
msg_dir = f"data/raw/telegram_messages/{today}"
img_dir = f"data/raw/images/{today}"
os.makedirs(msg_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

# Logging setup
log_file = f"logs/scraper_{today}.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Main scraper
async def scrape_channel(client, name, link):
    messages = []
    channel_img_dir = os.path.join(img_dir, name)
    os.makedirs(channel_img_dir, exist_ok=True)

    try:
        async for message in client.iter_messages(link, limit=200):
            msg = message.to_dict()

            if message.media and isinstance(message.media, MessageMediaPhoto):
                img_path = os.path.join(channel_img_dir, f"{message.id}.jpg")
                await message.download_media(file=img_path)
                msg["downloaded_image_path"] = img_path

            messages.append(msg)

        # Save messages
        out_path = os.path.join(msg_dir, f"{name}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

        logging.info(f"Scraped {len(messages)} messages from {name}")

    except Exception as e:
        logging.error(f"Failed scraping {name}: {e}")

# Entry point
async def main():
    async with TelegramClient("session_scraper", api_id, api_hash) as client:
        for name, link in channels.items():
            logging.info(f"🔁 Starting {name}")
            await scrape_channel(client, name, link)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
