from schemas.ChatMessage.GetChatMessage import GetChatMessages
from schemas.ChatMessage.CreateChatMessage import CreateChatMessage
from models.ChatMessage import ChatMessage
from app.dependencies import storage, manager

def get_messages():
    chats = storage.get_chats()
    return GetChatMessages(chatMessages= chats, count= len(chats))

async def post_message(createMessage:CreateChatMessage):
    chat = ChatMessage(**createMessage.model_dump(mode="json"))
    storage.add_chat(chat=chat) 
    await manager.broadcast(chat.model_dump(mode="json"))
    return chat