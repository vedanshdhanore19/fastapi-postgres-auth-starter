from fastapi import APIRouter
from app.models.drone import DroneLog

router = APIRouter(prefix="/drone", tags=["Drone Logging"])

@router.post("/log")
def log_telemetry(data: DroneLog):
    return{
        "status": "success",
        "message": f"Logged data for Drone #{data.drone_id}",
        "received_data": data
    }