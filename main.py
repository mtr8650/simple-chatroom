from fastapi import FastAPI
from models import Message
from database import init_db
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ Allows requests from any website (frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/send")
async def send_message(msg: dict):
    text = msg.get("text")

    # ✅ FIX: Ensure MongoDB Query Returns Messages
    if text.lower() == "history":
        messages = await Message.find_all().sort("+timestamp").to_list()
        if not messages:
            return {"history": []}  # Return an empty list instead of nothing

        return {
            "history": [{"text": m.text, "timestamp": str(m.timestamp)} for m in messages]
        }

    # ✅ FIX: Store Messages in MongoDB
    message = Message(text=text)
    await message.insert()
    return {"message": "Message saved"}
