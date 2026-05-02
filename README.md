# 🚀 Scalable URL Shortener

A production-ready URL shortener built using **FastAPI** and **MongoDB Atlas**, designed to handle real-time redirection and analytics. This project demonstrates backend system design, API development, and cloud deployment.

---

## 🌐 Live Demo

🔗 https://url-shortener-idtq.onrender.com
📄 API Docs: https://url-shortener-idtq.onrender.com/docs

---

## ✨ Features

* 🔗 Generate short URLs for long links
* ⚡ Fast redirection using HTTP 307
* 📊 Click tracking and analytics
* 🧠 Random unique short code generation (Base62-style)
* ✏️ Custom alias support (user-defined short URLs)
* ☁️ Cloud database integration (MongoDB Atlas)
* 🚀 Deployed on cloud (Render)

---

## 🏗️ System Architecture

Client → FastAPI → MongoDB Atlas
      ↘ Redirect + Analytics

* FastAPI handles API requests and routing
* MongoDB stores URL mappings and click data
* Analytics updates occur during each redirect

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** MongoDB Atlas
* **Deployment:** Render
* **Language:** Python

---

## 📡 API Endpoints

### 🔹 Create Short URL

`POST /shorten`

```json
{
  "long_url": "https://example.com",
  "custom_code": "optional"
}
```

---

### 🔹 Redirect to Original URL

`GET /{short_code}`

➡️ Redirects to the original URL

---

### 🔹 Get Analytics

`GET /stats/{short_code}`

```json
{
  "short_code": "abc123",
  "long_url": "https://example.com",
  "clicks": 10
}
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/url_shortener.git
cd url_shortener

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

uvicorn main:app --reload
```

---
## 📸 Screenshots

### 🔹 API Documentation (Swagger UI)
![Swagger UI](screenshots/swagger.png)

### 🔹 Short URL Generation
![Shorten](screenshots/shorten.png)

### 🔹 Redirect Working
![Redirect](screenshots/redirect.png)

### 🔹 Analytics (Click Tracking)
![Stats](screenshots/stats.png)
 
 ----

## 🔐 Environment Variables

Create a `.env` file:

```
MONGO_URL=your_mongodb_atlas_connection_string
```

---

## 🧠 Design Decisions

* **Random Short Codes:** Avoids predictability and collision issues from sequential IDs
* **MongoDB:** Flexible schema for storing URL mappings and analytics
* **Cloud Deployment:** Ensures accessibility and scalability
* **Analytics Tracking:** Simulates real-world usage monitoring

---
## ⚡Scalability Considerations
* Designed for high read traffic (redirect-heavy system)
* Short URL lookup optimized for fast database queries
* Stateless backend enables horizontal scaling
* Future enhancement: Redis caching to reduce database load
  
---
## 🔄 How It Works
* User sends a long URL to /shorten
* server generates a unique short code
* URL mapping is stored in MongoDB
* User accesses the short URL
* Server retrieves original URL and redirects
* Click count is updated for analytics
  
--- 

## 🧩 Challenges & Solutions
* **Problem:** Duplicate short codes due to counter reset
  **Solution:** Switched to random Base62-style code generation
* **Problem:** MongoDB connection errors due to special characters
  **Solution:** Used proper URL encoding for credentials
* **Problem:** Incorrect URL formatting causing redirect issues
  **Solution:** Added validation and ensured clean input handling

---

## 🚀 Future Improvements

* ⚡ Redis caching for faster lookups
* 🔒 Authentication & user-specific URLs
* ⏳ Expiry for short links
* 📊 Dashboard UI for analytics
* 🌍 Custom domain support

---

## 📌 Conclusion

This project demonstrates the design and deployment of a scalable backend system with real-world features like URL redirection, analytics tracking, and cloud integration.

---

## 👩‍💻 Author

Kaviya
B.Tech Artificial Intelligence & Data Science
Aspiring Software Engineer

---
