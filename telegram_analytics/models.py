from pydantic import BaseModel
from datetime import datetime
from typing import List

class Message(BaseModel):
    message_id: str
    message_text: str
    channel_id: str
    sent_at: datetime
    has_image: bool
    message_length: int

class TopProduct(BaseModel):
    product: str
    mentions: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int
