import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import User
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Функция подключения к MongoDB и инициализации моделей Beanie
async def init_db():
    client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
    await init_beanie(database=client.get_default_database(), document_models=[User])
