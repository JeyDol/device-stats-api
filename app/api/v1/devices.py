from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.repositories.device import DeviceRepository
from app.repositories.measurement import MeasurementRepository
from app.schemas.device import DeviceCreate, DeviceRead
from app.schemas.measurement import MeasurementCreate
from app.schemas.stats import StatsRead
from app.services.device import DeviceService
from app.services.measurement import MeasurementService

router = APIRouter(prefix="/devices", tags=["Devices"])


@router.post("", response_model=DeviceRead)
async def create_device(
    data: DeviceCreate,
    session: AsyncSession = Depends(get_session)
):
    service = DeviceService(DeviceRepository(session))
    return await service.create_device(data)


@router.post("/{device_id}/measurements")
async def add_measurement(
    device_id: int,
    data: MeasurementCreate,
    session: AsyncSession = Depends(get_session)
):
    service = MeasurementService(MeasurementRepository(session))
    return await service.add_measurement(device_id, data)


@router.get("/{device_id}/stats", response_model=StatsRead)
async def get_stats(
    device_id: int,
    from_dt: datetime | None = None,
    to_dt: datetime | None = None,
    session: AsyncSession = Depends(get_session)
):
    service = MeasurementService(MeasurementRepository(session))
    if from_dt and to_dt:
        return await service.get_stats_by_period(device_id, from_dt, to_dt)
    return await service.get_stats(device_id)