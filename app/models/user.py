from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
