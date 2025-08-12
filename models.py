from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    name: str
    email: EmailStr

    class Settings:
        name = "users"  # Name of collection in MongoDB

class UserCreate(BaseModel):
    name: str
    email: EmailStr
