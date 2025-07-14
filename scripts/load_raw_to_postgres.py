import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def load_json_to_db(json_path):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    with open(json_path, "r", encoding="utf-8") as f:
        messages = json.load(f)

    for msg in messages:
        cur.execute(
            "INSERT INTO raw.telegram_messages_raw (data) VALUES (%s)",
            [json.dumps(msg)]
        )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    import glob
    import datetime

    today = datetime.datetime.today().strftime("%Y-%m-%d")
    files = glob.glob(f"data/raw/telegram_messages/{today}/*.json")

    for file in files:
        print(f"Loading {file} into PostgreSQL...")
        load_json_to_db(file)
