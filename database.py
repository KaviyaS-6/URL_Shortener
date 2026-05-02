import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["url_db"]
collection = db["urls"]
