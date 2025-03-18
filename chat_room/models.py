from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class Message(Document):
    text: str
    timestamp: datetime = datetime.utcnow()

    class Settings:
        collection = "messages"

class MessageCreate(BaseModel):
    text: str
