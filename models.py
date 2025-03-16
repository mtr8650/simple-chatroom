from beanie import Document
from datetime import datetime

class Message(Document):
    text: str
    timestamp: datetime = datetime.utcnow()
