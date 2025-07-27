import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport
from datetime import datetime
from websockets import connect
import sys
import os
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from app.config import DOMAIN
        

@pytest.mark.asyncio
async def test_post_alert():
    ws_uri = f"ws://{DOMAIN}/ws"

    async with connect(ws_uri) as websocket:
        async with AsyncClient(base_url=f"http://{DOMAIN}") as ac:
            payload = {
                "message": "Puerta abierta sin autorización",
                "location": "Puerta Sur"
            }
            post_response = await ac.post("/alerts", json=payload)
            assert post_response.status_code == 200

            response_json = post_response.json()

            assert "id" in response_json
            assert "timestamp" in response_json
            assert "type" in response_json
            assert "message" in response_json
            assert "location" in response_json

            # Validar valores esperados
            assert response_json["type"] == "alert"
            assert response_json["message"] == "Puerta abierta sin autorización"
            assert response_json["location"] == "Puerta Sur"

            uuid.UUID(response_json["id"])

            datetime.fromisoformat(response_json["timestamp"])
        



@pytest.mark.asyncio
async def test_get_history():
    async with AsyncClient(base_url=f"http://{DOMAIN}") as ac:
        get_response = await ac.get("/alerts/history")
        assert get_response.status_code == 200

        history = get_response.json()
        assert isinstance(history, dict)
        assert "alerts" in history
        assert isinstance(history["alerts"], list)

        alerts = history["alerts"]
        assert len(alerts) >= 1
        assert "message" in alerts[-1]

