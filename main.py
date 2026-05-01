from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from database import collection
from models import generate_code

app = FastAPI()


# Request model
class URLRequest(BaseModel):
    long_url: str
    custom_code: str | None = None


# Home route
@app.get("/")
def home():
    return {"message": "URL Shortener API is running 🚀"}


# Create short URL
@app.post("/shorten")
def shorten_url(request: URLRequest):
    long_url = request.long_url
    custom_code = request.custom_code

    # if user gives custom code
    if custom_code:
        existing = collection.find_one({"short_code": custom_code})
        if existing:
            return {"error": "Custom code already exists"}

        short_code = custom_code
    else:
        short_code = generate_code()

    collection.insert_one({
        "long_url": long_url,
        "short_code": short_code,
        "clicks": 0
    })

    return {"short_url": f"http://localhost:8000/{short_code}"}

# Redirect to original URL
@app.get("/{short_code}")
def redirect_url(short_code: str):
    data = collection.find_one({"short_code": short_code})

    if data:
        # Increase click count
        collection.update_one(
            {"short_code": short_code},
            {"$inc": {"clicks": 1}}
        )

        return RedirectResponse(url=data["long_url"])

    return {"error": "URL not found"}


# View analytics
@app.get("/stats/{short_code}")
def get_stats(short_code: str):
    data = collection.find_one({"short_code": short_code})

    if data:
        return {
            "long_url": data["long_url"],
            "short_code": data["short_code"],
            "clicks": data["clicks"]
        }

    return {"error": "Not found"}


# Reset database
@app.delete("/reset")
def reset_database():
    collection.delete_many({})
    return {"message": "All URLs deleted successfully"}

#Stats API
@app.get("/stats/{short_code}", operation_id="get_url_stats")
def get_url_stats(short_code: str):
    data = collection.find_one({"short_code": short_code})

    if data:
        return {
            "short_code": data["short_code"],
            "long_url": data["long_url"],
            "clicks": data.get("clicks", 0)
        }

    return {"error": "Not found"}
