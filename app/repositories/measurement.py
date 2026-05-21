from datetime import datetime

from sqlalchemy import select

from app.models.measurement import MeasurementOrm
from app.repositories.base import BaseRepository


class MeasurementRepository(BaseRepository):
    model = MeasurementOrm


    async def get_by_device_id(self, device_id: int):
        """Получить все измерения"""
        result = await self.session.execute(
            select(self.model).where(MeasurementOrm.device_id == device_id)
        )
        return result.scalars().all()


    async def get_by_device_id_and_period(self, device_id: int, from_dt: datetime, to_dt: datetime) -> list[MeasurementOrm]:
        """Получить измерения за какой-то период"""
        result = await self.session.execute(
            select(self.model).where(
                MeasurementOrm.device_id == device_id,
                MeasurementOrm.timestamp >= from_dt,
                MeasurementOrm.timestamp <= to_dt
            )
        )
        return result.scalars().all()