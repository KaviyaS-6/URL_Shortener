from pymongo import MongoClient

client = MongoClient("mongodb+srv://skaviya:Kaviya%4023@url-shortener-cluster.9lqhait.mongodb.net/?retryWrites=true&w=majority")
db = client["url_db"]
collection = db["urls"]