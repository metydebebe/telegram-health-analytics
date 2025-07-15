from database import get_db_connection

def get_top_products(limit: int = 10):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT product, COUNT(*) as mentions 
            FROM fct_image_detections
            GROUP BY product
            ORDER BY mentions DESC
            LIMIT %s;
        """, (limit,))
        rows = cur.fetchall()
    conn.close()
    return [{"product": row[0], "mentions": row[1]} for row in rows]

def get_channel_activity(channel_name: str):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT DATE(sent_at), COUNT(*) 
            FROM fct_messages
            WHERE channel_id = %s
            GROUP BY DATE(sent_at)
            ORDER BY DATE(sent_at);
        """, (channel_name,))
        rows = cur.fetchall()
    conn.close()
    return [{"date": str(row[0]), "message_count": row[1]} for row in rows]

def search_messages(query: str):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT message_id, message_text, channel_id, sent_at, has_image, LENGTH(message_text) 
            FROM fct_messages
            WHERE message_text ILIKE %s;
        """, (f"%{query}%",))
        rows = cur.fetchall()
    conn.close()
    return [{
        "message_id": row[0],
        "message_text": row[1],
        "channel_id": row[2],
        "sent_at": row[3],
        "has_image": row[4],
        "message_length": row[5]
    } for row in rows]
