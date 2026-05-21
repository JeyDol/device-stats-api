from datetime import datetime

from pydantic import BaseModel


class MeasurementCreate(BaseModel):
    x: float
    y: float
    z: float


class MeasurementRead(BaseModel):
    id: int
    device_id: int
    x: float
    y: float
    z: float
    timestamp: datetime