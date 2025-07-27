from models.Alerts import AlertMessage
from pydantic import BaseModel
from typing import List

class GetAlerts(BaseModel):
    alerts: List[AlertMessage]= []
    count: int