from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import init_db  # Database initialization
from routes import router  # Import routes
from fastapi.middleware.cors import CORSMiddleware

# ✅ Use Lifespan to manage startup events
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # ✅ Initializes MongoDB on startup
    yield  # ✅ Allows the app to continue running

# ✅ Initialize FastAPI app with Lifespan
app = FastAPI(lifespan=lifespan)

# ✅ Include API routes
app.include_router(router)

# ✅ Enable CORS (Allows frontend to make requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


