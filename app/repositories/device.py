from sqlalchemy import select

from app.models.device import DeviceOrm
from app.repositories.base import BaseRepository


class DeviceRepository(BaseRepository):
    model = DeviceOrm


    async def get_all_by_user_id(self, user_id: int) -> list[DeviceOrm]:
        """Получить все устройства пользователя"""
        result = await self.session.execute(
            select(self.model).where(DeviceOrm.user_id == user_id)
        )
        return result.scalars().all()