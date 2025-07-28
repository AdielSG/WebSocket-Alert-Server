# 🚨 Real-Time Alert Backend (FastAPI + WebSocket)

This project is a backend server that powers a real-time alert dashboard. It provides both a REST API and WebSocket server to handle automated alerts, chat messages, and manual event triggering.

## ⚠️ How alerts and chat messages are handled and stored in memory

The system uses a custom-built StorageManager that handles both alert and chat message persistence using Python’s deque from the collections module. This structure efficiently stores only the last 10 alerts and last 10 chat messages, automatically discarding the oldest entries when new ones are added. This ensures memory usage remains minimal and consistent, in line with the technical requirement to avoid database usage.

Both REST and WebSocket operations interact with this in-memory manager to retrieve or store messages in real-time.

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
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
```

3. **Activate the Virtual Environment**

Use the appropriate command depending on your operating system:

• Windows (PowerShell):
```bash
.\venv\Scripts\activate.ps1
```

• Windows (Command Prompt):
```bash
venv\Scripts\activate.bat
```

• macOS / Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Create a `.env` file at the root of the project with the following environment variables**

```bash
CORS_ORIGINS_ALLOWED=http://localhost:3000  # Frontend origins allowed
CORS_CREDENTIAL=true                        # Whether to allow credentials
CORS_METHODS_ALLOWED=POST,GET               # HTTP methods to allow
CORS_HEADERS_ALLOWED=Authorization          # Headers to allow
DOMAIN=127.0.0.1:8000                       # Your app domain (e.g. localhost:8000)

```
🔧 Replace the values as needed for your local or deployed environment.

6. **Run the server**

```bash
uvicorn app.main:app --reload
```
---

## 📡 WebSocket

1. **Connect to the WebSocket using Postman or any WebSocket client**

Use the following URL to connect locally:

```bash
ws://localhost:8000/ws
```

**Or**, if you want to test the deployed version (note that due to the free hosting tier, the server may take a few seconds to wake up after being idle), use:

```bash
ws://websocket-alert-server.onrender.com/ws
```

2. **Automatic alerts (every 10 seconds):**

The server automatically generates and broadcasts an alert every 10 seconds. The alert follows this structure:

```json
{
  "id": "uuid4",
  "message": "Intruder detected",
  "location": "North Gate",
  "timestamp": "2025-07-24T14:23:00Z",
  "type": "alert"
}
```

3. **Sending chat messages:**

When a user sends a chat message, it is broadcasted to all connected clients in the following format:

```json
{
    "id": "7bb4eacd-9d48-4fff-a9d0-a7caffbd52a8",
    "timestamp": "2025-07-28T12:24:44.157040",
    "type": "chat",
    "sender": "Jose",
    "message": "Please check the back door"
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

`POST /message`

Send a manual message and broadcast it to WebSocket clients.

**Request:**

```json
{
    "sender": "Jose",
    "message": "Please check the back door"
}
```

**Response:**

```json
{
    "id": "3c248f90-0242-4685-a8b3-8e84e1b226a9",
    "timestamp": "2025-07-28T00:01:58.036234",
    "type": "chat",
    "sender": "Jose",
    "message": "Please check the back door"
}
```

`GET /message`

Get the last 10 chat messages stored in memory

**Response:**
```json
{
    "chatMessages": [
        {
            "id": "3c248f90-0242-4685-a8b3-8e84e1b226a9",
            "timestamp": "2025-07-28T00:01:58.036234",
            "type": "chat",
            "sender": "Jose",
            "message": "Please check the back door"
        }
    ],
    "count": 1
}
```

---

## 🧠 Project Structure

```bash
.
├── app/
│   ├── main.py               # FastAPI app with lifespan + setup
│   ├── config.py             # App configuration
│   └── dependencies.py        # Shared dependencies (if needed)
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