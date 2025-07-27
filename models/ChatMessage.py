from models.Messages import Message

class ChatMessage(Message):
    sender: str
    message: str
