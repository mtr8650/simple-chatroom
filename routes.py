from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()  # Create a router object

# Define request model for sending messages
class MessageRequest(BaseModel):
    text: str

# In-memory storage for chat history
chat_history = ["Hello!", "How are you?", "Welcome!"]

# ✅ `POST` to send a message
@router.post("/send")
async def send_message(msg: MessageRequest):
    if msg.text == "history":
        return {"history": chat_history}
    chat_history.append(msg.text)
    return {"message": "Message received"}

# ✅ `GET` to retrieve chat history
@router.get("/history")
async def get_history():
    return {"history": chat_history}
