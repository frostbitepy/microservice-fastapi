import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://fran94rv:test123@cluster0.zlvwasb.mongodb.net/?retryWrites=true&w=majority"
  # Create a new client and connect to the server
client = AsyncIOMotorClient(uri)
db = client.vida_database
collection = db["cumulo_collection"]


async def ping_server():
  # Replace the placeholder with your Atlas connection string
  uri = "mongodb+srv://fran94rv:test123@cluster0.zlvwasb.mongodb.net/?retryWrites=true&w=majority"
  # Create a new client and connect to the server
  client = AsyncIOMotorClient(uri)
  # Send a ping to confirm a successful connection
  try:
      await client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
      print(e)
      

if __name__ == "__main__":
    asyncio.run(ping_server())
