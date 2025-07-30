from beanie import Document
from pydantic import BaseModel, EmailStr
from typing import Optional

# Это модель, которая хранится в базе данных
class User(Document):
    name: str
    email: EmailStr

    class Settings:
        name = "users"  # Название коллекции в MongoDB

# Это модель, которую мы используем при создании пользователя (валидируем входные данные)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
