from app.repositories.device import DeviceRepository
from app.schemas.device import DeviceCreate
from app.services.base import BaseService


class DeviceService(BaseService):
    def __init__(self, repository: DeviceRepository):
        super().__init__(repository)
        self.repository: DeviceRepository = repository

    async def create_device(self, data: DeviceCreate):
        """Создать устройство"""
        return await self.repository.create(data.model_dump())


    async def get_device(self, device_id: int):
        """Получить устройство по id"""
        return await self.repository.get_by_id(device_id)


    async def get_devices_by_user(self, user_id: int):
        """Получить все устройства пользователя"""
        return await self.repository.get_all_by_user_id(user_id)