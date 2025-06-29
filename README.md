---

## 🔗 Bitly Clone – URL Shortener (FastAPI + React + Redis)

A full-stack URL shortener inspired by Bitly. The backend is built with **FastAPI**, uses **Redis** for caching, and the frontend is a **React** application. Everything is containerized using **Docker Compose**.

![image](https://github.com/user-attachments/assets/821ce622-c63b-4b6f-81f5-185b829790c1)

---

## 💬 High Level Architecture Diagram

![image](https://github.com/user-attachments/assets/600edfa2-29f8-445b-98b7-273dd629f7e2)


---

### 🚀 Features

* 🔗 Shorten long URLs into simple 6-character codes
* ⚡ Fast redirection powered by Redis caching
* 🔁 Usage count tracking
* 🖥️ React-based frontend UI
* 🐳 Fully containerized with Docker Compose

---

### ⚙️ Docker Setup

#### ✅ Start the App

```bash
docker-compose up --build
```

#### 📌 Services Overview

| Service  | Description           | URL                                                    |
| -------- | --------------------- | ------------------------------------------------------ |
| `client` | React frontend        | [http://localhost:8080](http://localhost:8080)         |
| `server` | FastAPI backend (API) | [http://localhost:8000/api](http://localhost:8000/api) |
| `redis`  | Redis cache           | Internal only                                          |

---

### 📦 API Endpoints

#### `POST /api/shorten`

Creates a new short URL.

* **Request JSON**:

  ```json
  {
    "longUrl": "https://example.com"
  }
  ```

* **Response**:

  ```json
  {
    "short_url": "a1B2c3"
  }
  ```

---

#### `GET /api/{short_code}`

Redirects to the original URL and increments usage count.

* Example:
  `GET /api/a1B2c3` → Redirects to `https://example.com`

---

### 🧪 Environment Variables

Create a `.env` file in the project root (used by the backend):

```env
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/dbname
REDIS_HOST=redis
REDIS_PORT=6379
```

Make sure these are referenced in `server/db.py` and `redis_client.py`.

---

### 📸 Frontend Preview

Once the project is running:

* Access the **React frontend** at: [http://localhost:5173](http://localhost:5173)
* It interacts with the backend at `/api`

---

### 👨‍💻 Author

Built with ❤️ by [Sunil Swizy](https://github.com/sunilswizy)

---
