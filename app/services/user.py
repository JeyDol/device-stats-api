from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.services.base import BaseService


class UserService(BaseService):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.repository: UserRepository = repository

    async def create_user(self, data: UserCreate):
        """Создание пользователя"""
        return await self.repository.create(data.model_dump())


    async def get_user(self, user_id: int):
        """Получить пользователя по id"""
        return await self.repository.get_by_id(user_id)