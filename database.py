import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import User
from dotenv import load_dotenv

# Loading variables from .env file
load_dotenv()

# Function to connect to MongoDB and initialize Beanie models
async def init_db():
    client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
    await init_beanie(database=client.get_default_database(), document_models=[User])
