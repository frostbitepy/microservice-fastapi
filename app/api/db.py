import os
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = 'movie_db'

class Movie(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    name: str
    plot: str
    genres: List[str]
    casts: List[str]

async def connect_to_mongo():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[DATABASE_NAME]
    return db

async def close_mongo_connection(db):
    db.client.close()

