# utils/database.py
from datetime import datetime
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["discord_bot"]
history_collection = db["chat_history"]

def save_chat_history(user_id, guild_id, prompt, response):
    history_collection.insert_one({
        "user_id": str(user_id),
        "guild_id": str(guild_id) if guild_id else None,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.utcnow()
    })
