from fastapi import FastAPI
from contextlib import asynccontextmanager
from chat_room.routes import router
from chat_room.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # Initialize the database
    yield  # Continue running the app

app = FastAPI(title="Chat Room API", lifespan=lifespan)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Chat Room API is running!"}


from fastapi.responses import Response

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)  # No Content
