from beanie import Document
from datetime import datetime, timezone
class Message(Document):
    text: str
    timestamp: datetime = datetime.now(timezone.utc)