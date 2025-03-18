from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from chat_room.models import Message

MONGO_URI = "mongodb://localhost:27017/chatdb"

client = AsyncIOMotorClient(MONGO_URI)
database = client.get_database()

async def init_db():
    await init_beanie(database, document_models=[Message])
