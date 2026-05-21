from datetime import datetime

from sqlalchemy import String, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base


class DeviceOrm(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())