# utils/database.py

import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGO_DB_NAME", "mydiscordbot")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

# collections mẫu
users = db["users"]
guilds = db["guilds"]
