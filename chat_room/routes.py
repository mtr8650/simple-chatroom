from fastapi import APIRouter, HTTPException
from chat_room.models import Message, MessageCreate
from typing import List

router = APIRouter()

@router.post("/send", response_model=Message)
async def send_message(msg: MessageCreate):
    message = Message(text=msg.text)
    await message.insert()
    return message

@router.get("/history", response_model=List[Message])
async def get_messages():
    return await Message.find_all().sort("+timestamp").to_list()
