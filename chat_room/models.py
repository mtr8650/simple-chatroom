from beanie import Document
from pydantic import BaseModel, EmailStr
from datetime import datetime
from passlib.context import CryptContext

class Message(Document):
    text: str
    timestamp: datetime = datetime.utcnow()

    class Settings:
        collection = "messages"

class MessageCreate(BaseModel):
    text: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Document):
    username: str
    email: EmailStr
    hashed_password: str

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.hashed_password)

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
