from pydantic import BaseModel

class TopProduct(BaseModel):
    product: str
    count: int

class ChannelActivity(BaseModel):
    date: str  # YYYY-MM-DD
    message_count: int

class MessageSearchResult(BaseModel):
    message_id: str
    channel_id: str
    sent_at: str
    message_text: str
