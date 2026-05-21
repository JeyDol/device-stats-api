from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class MeasurementOrm(Base):
    __tablename__ = "measurements"

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))
    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()
    z: Mapped[float] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(server_default=func.now())
