from sqlalchemy import select

from app.models.user import UserOrm
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    model = UserOrm


    async def get_by_username(self, username: str) -> UserOrm | None:
        """Получить пользователя по username"""
        result = await self.session.execute(
            select(self.model).where(self.model.username == username)
        )
        return result.scalar_one_or_none()