from datetime import datetime

from pydantic import BaseModel


class DeviceCreate(BaseModel):
    name: str
    user_id: int | None


class DeviceRead(BaseModel):
    id: int
    name: str
    user_id: int | None
    created_at: datetime