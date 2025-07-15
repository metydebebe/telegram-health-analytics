from fastapi import FastAPI
from typing import List
from models import TopProduct, ChannelActivity, Message
from crud import get_top_products, get_channel_activity, search_messages

app = FastAPI(title="Telegram Analytics API")

@app.get("/api/reports/top-products", response_model=List[TopProduct])
def top_products(limit: int = 10):
    return get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity", response_model=List[ChannelActivity])
def channel_activity(channel_name: str):
    return get_channel_activity(channel_name)

@app.get("/api/search/messages", response_model=List[Message])
def search(query: str):
    return search_messages(query)
