from fastapi import WebSocket, WebSocketDisconnect
from models.ChatMessage import ChatMessage
from pydantic import ValidationError
from app.dependencies import storage, manager

async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            try:
                chat = ChatMessage(**data)
                storage.add_chat(chat=chat)

                await manager.broadcast(chat.model_dump(mode="json"))
            except ValidationError as e:
                print("Ha ocurrido un error de serializacion")
                await websocket.send_json({
                    "type": "error",
                    "message": "Invalid chat message. Expected: sender (str), message (str)."
                })
                continue

    except WebSocketDisconnect:
        manager.disconnect(websocket)