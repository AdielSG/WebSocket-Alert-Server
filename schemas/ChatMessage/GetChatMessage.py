from models.ChatMessage import ChatMessage
from pydantic import BaseModel
from typing import List

class GetChatMessages(BaseModel):
    chatMessages: List[ChatMessage]= []
    count: int