from datetime import datetime

from app.repositories.measurement import MeasurementRepository
from app.schemas.measurement import MeasurementCreate
from app.services.base import BaseService

from app.tasks.analytics import calculate_stats


class MeasurementService(BaseService):
    def __init__(self, repository: MeasurementRepository):
        super().__init__(repository)
        self.repository: MeasurementRepository = repository

    def _calculate_stats(self, measurements):
        """Подсчет статистики"""
        values = []
        for m in  measurements:
            values.extend([m.x, m.y, m.z])
        values.sort()

        return {
            "min": min(values),
            "max": max(values),
            "count": len(values),
            "sum": sum(values),
            "median": values[len(values) // 2]
        }


    async def add_measurement(self, device_id: int, data: MeasurementCreate):
        """Добавить показание"""
        payload = data.model_dump()
        payload["device_id"] = device_id
        return await self.repository.create(payload)


    async def get_stats(self, device_id: int):
        """Получить статистику за все время"""
        measurements = await self.repository.get_by_device_id(device_id)
        measurements_data = [{"x": m.x, "y": m.y, "z": m.z} for m in measurements]
        task = calculate_stats.delay(measurements_data)
        return task.get()


    async def get_stats_by_period(self, device_id: int, from_dt: datetime, to_dt: datetime):
        """Получить статистику за период"""
        measurements = await self.repository.get_by_device_id_and_period(device_id, from_dt, to_dt)
        measurements_data = [{"x": m.x, "y": m.y, "z": m.z} for m in measurements]
        task = calculate_stats.delay(measurements_data)
        return task.get()