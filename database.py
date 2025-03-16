from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import Message

async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")  # Connect to local MongoDB
    await init_beanie(database=client.chat_db, document_models=[Message])