from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.repositories.device import DeviceRepository
from app.repositories.measurement import MeasurementRepository
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.services.device import DeviceService
from app.services.measurement import MeasurementService
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("")
async def create_user(
    data: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    service = UserService(UserRepository(session))
    return await service.create_user(data)


@router.get("/{user_id}/stats")
async def get_stats_for_user(
    user_id: int,
    session: AsyncSession = Depends(get_session)
):
    device_service = DeviceService(DeviceRepository(session))
    measurement_service = MeasurementService(MeasurementRepository(session))

    devices = await device_service.get_devices_by_user(user_id)

    result = {}
    for device in devices:
        result[device.id] = await measurement_service.get_stats(device.id)
    return result