import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "telegram_analytics"))
import psycopg2
import json
# from config import DATABASE_URL

def load_yolo_results():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    with open("data/yolo_results.json", "r") as f:
        detections = json.load(f)
        for det in detections:
            cur.execute("""
                INSERT INTO raw_yolo_detections (image_path, class_id, confidence)
                VALUES (%s, %s, %s)
            """, (det["image"], det["class"], det["confidence"]))

    conn.commit()
    cur.close()
    conn.close()
