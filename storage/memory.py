from typing import List
from models.ChatMessage import ChatMessage
from models.Alerts import AlertMessage
from collections import deque
import threading

class InMemoryStorage:
    def __init__(self, max_alerts: int =10, max_chats: int = 10):
        self.alerts: deque[AlertMessage] = deque(maxlen=max_alerts)
        self.chats: deque[ChatMessage] = deque(maxlen=max_chats)
        self.lock = threading.Lock()

    def add_alert(self, alert: AlertMessage):
        with self.lock:
            self.alerts.append(alert)

    def get_alerts(self) -> List[AlertMessage]:
        with self.lock:
            return list(self.alerts)
        
    def add_chat(self, chat: ChatMessage):
        with self.lock:
            self.chats.append(chat)

    def get_chats(self) -> List[ChatMessage]:
        with self.lock:
            return list(self.chats)