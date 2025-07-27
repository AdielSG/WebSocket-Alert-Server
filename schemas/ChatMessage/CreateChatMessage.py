from models.Messages import Message

class CreateChatMessage(Message):
    sender: str
    message: str