from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.SecurityHeadersMiddleware import SecurityHeadersMiddleware
from app.config import CORS_ORIGINS, CORS_CREDENTIAL, CORS_METHODS_ALLOWED, CORS_HEADERS_ALLOWED
from routes import alerts, messages
from lifespan.alerts_lifespan import lifespan
from WebSockets.chat_ws import websocket_endpoint


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=CORS_CREDENTIAL,
    allow_methods=CORS_METHODS_ALLOWED,
    allow_headers=CORS_HEADERS_ALLOWED
)

app.add_middleware(SecurityHeadersMiddleware)

app.include_router(alerts.router)
app.include_router(messages.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to my WebSocket Application"}


app.websocket("/ws")(websocket_endpoint)
    