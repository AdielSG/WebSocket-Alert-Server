import asyncio
from contextlib import asynccontextmanager
from models.Alerts import AlertMessage
from fastapi import FastAPI
from app.dependencies import storage, manager


@asynccontextmanager
async def lifespan(app:FastAPI):
    async def send_alert_automatic():
        while True:
            alert = AlertMessage(message="Intruder detected", location="North Gate", type="alert")
            storage.add_alert(alert=alert)
            await manager.broadcast(alert.model_dump(mode="json"))
            await asyncio.sleep(10)
    
    task = asyncio.create_task(send_alert_automatic())

    yield
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass