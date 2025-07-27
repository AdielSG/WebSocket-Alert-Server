# 🚨 Real-Time Alert Backend (FastAPI + WebSocket)

This project is a backend server that powers a real-time alert dashboard. It provides both a REST API and WebSocket server to handle automated alerts, chat messages, and manual event triggering.

---

## 🚀 Tech Stack

- 🐍 Python 3.11+
- ⚡ FastAPI
- 🔌 WebSocket via `ConnectionManager`
- 🧠 In-memory storage (`InMemoryStorage`)
- 🧪 Pytest + HTTPX for testing
- 🌐 CORS and security headers middleware

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/AdielSG/WebSocket-Alert-Server.git
cd Technica_Test
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the server**

```bash
uvicorn app.main:app --reload
```

---

## 📡 WebSocket

1. **Connect to**

```bash
ws://localhost:8000/ws
```

2. **Automatic alerts (every 10 seconds):**

```json
{
  "id": "uuid4",
  "message": "Intruder detected",
  "location": "North Gate",
  "timestamp": "2025-07-24T14:23:00Z",
  "type": "alert"
}
```

3. **Send chat messages:**

```json
{
  "sender": "Operator 1",
  "message": "What’s happening at North Gate?"
}
```

All chat messages are broadcasted to connected clients.

---

## 📥 REST API Endpoints

`POST /alerts`

Send a manual alert and broadcast it to WebSocket clients.

**Request:**

```json
{
  "message": "Unauthorized door access",
  "location": "South Gate"
}
```

**Response:**

```json
{
  "id": "uuid", //auto-generated uuid
  "timestamp": "2025-07-27T00:41:19.647092",
  "type": "alert",
  "message": "Unauthorized door access",
  "location": "South Gate"
}
```

`GET /alerts/history`

Get the last 10 alerts stored in memory

**Response:**

```json
{
  "alerts": [
    {
      "id": "uuid", //auto-generated uuid
      "timestamp": "2025-07-27T00:41:19.647092",
      "type": "alert",
      "message": "Unauthorized door access",
      "location": "South Gate"
    },
    {
      "id": "uuid", //auto-generated uuid
      "timestamp": "2025-07-27T00:41:19.647092",
      "type": "alert",
      "message": "Unauthorized door access",
      "location": "South Gate"
    },
    {
      "id": "uuid", //auto-generated uuid
      "timestamp": "2025-07-27T00:41:19.647092",
      "type": "alert",
      "message": "Unauthorized door access",
      "location": "South Gate"
    }
  ], // list of the last 10 alerts
  "count": 3 //number of the alerts available
}
```

---

## 🧠 Project Structure

```bash
.
├── app/
│   ├── main.py               # FastAPI app with lifespan + setup
│   ├── config.py             # App configuration
│   └── dependecies.py        # Shared dependencies (if needed)
├── routes/                   # REST API routers
├── controllers/             # Endpoint logic handlers
├── services/                # Business logic (alerts, chat)
├── models/                  # Data models
├── schemas/                 # Pydantic schemas for validation
├── storage/memory.py        # In-memory alert/message storage
├── WebSockets/              # WebSocket endpoint and manager
├── lifespan/                # Background task for alerts
├── middlewares/             # Security headers middleware
├── tests/                   # Unit tests for API and WebSocket
└── README.md
```
---

## 🧪 Running Tests
To run unit tests:
```bash
pytest
```
Covers:

• Manual alert insertion (POST /alerts)

• Alert history retrieval (GET /alerts/history)

• WebSocket connection and broadcasting

## ✅ Requirement Checklist

 • WebSocket server accepting connections✔️

 • Broadcasts alerts every 10 seconds✔️

 • Chat messages from clients broadcasted✔️

 • POST /alerts endpoint✔️

 • GET /alerts/history endpoint✔️

 • In-memory storage for alerts and messages✔️

 • Payload validation using Pydantic✔️

 • CORS and security headers middleware✔️

 • Unit tests included✔️

 • Clean architecture (routes, controllers, services, schemas)✔️