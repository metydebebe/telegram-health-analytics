import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import DATABASE_URL
import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
