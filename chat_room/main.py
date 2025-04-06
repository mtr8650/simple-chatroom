from fastapi import FastAPI
from contextlib import asynccontextmanager
from chat_room.routes import router
from chat_room.auth_routes import router as auth_router
from chat_room.database import init_db
from fastapi.responses import Response

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Chat Room API", lifespan=lifespan)

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Chat Room API is running!"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)
