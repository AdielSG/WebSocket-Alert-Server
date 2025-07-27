from fastapi import APIRouter
from schemas.ChatMessage.CreateChatMessage import CreateChatMessage
from controllers.message_controller import get_messages, post_message

router = APIRouter(prefix="/message", tags=["chat"])

@router.get("/")
def fetch_messages():
    return get_messages()

@router.post("/")
async def send_message(message: CreateChatMessage):
    return await post_message(message)