from pydantic import BaseModel, Field

class DroneLog(BaseModel):
    drone_id: int
    location: str
    battery_level: int = Field(ge=0, le=100)