import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def test_mongo():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.chat_db  # Make sure this matches your actual database
    messages = await db.message.find().to_list(length=10)

    if messages:
        for msg in messages:
            print(msg)
    else:
        print("❌ No messages found!")

asyncio.run(test_mongo())
