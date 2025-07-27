from fastapi import APIRouter
from schemas.Alerts.CreateAlert import CreateAlert
from controllers.alerts_controller import  get_alerts_history, post_alert


router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/history")
def get_alerts():
    return get_alerts_history()

@router.post("")
async def create_alert(alert: CreateAlert):
    return await post_alert(alert)