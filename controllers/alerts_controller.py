from models.Alerts import AlertMessage
from schemas.Alerts.GetAlerts import GetAlerts
from schemas.Alerts.CreateAlert import CreateAlert
from app.dependencies import storage, manager

def get_alerts_history():
    alerts = storage.get_alerts()
    return GetAlerts(alerts=alerts, count=len(alerts))

async def post_alert(data: CreateAlert):
    alert = AlertMessage(**data.model_dump(mode="json"))
    alert.type = "alert"
    storage.add_alert(alert)
    await manager.broadcast(alert.model_dump(mode="json"))
    return alert