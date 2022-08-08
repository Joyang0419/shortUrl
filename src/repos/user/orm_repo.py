"""ORM user repo implement"""

from typing import Optional

from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.entities import UserEntity
from src.orm_models.user import UserModel
from src.repos.user.exceptions import DuplicateAccountException
from src.repos.user.interface import UserRepoInterface


class ORMUserRepo(UserRepoInterface):
    account_model = UserModel

    def __init__(self, db_manager: AsyncORMDBManager):
        self.db_manager = db_manager

    async def get_user_by_account(
            self,
            account: str
    ) -> Optional[UserEntity]:
        stmt = select(self.account_model).where(
            self.account_model.account == account,
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        dto: Optional[UserModel] = result.scalars().one_or_none()

        if not dto:
            return None

        return UserEntity(
            id=dto.id,
            account=dto.account,
            hashed_password=dto.password,
        )

    async def get_user_by_id(
            self,
            user_id: int
    ) -> Optional[UserEntity]:
        stmt = select(self.account_model).where(
            self.account_model.id == user_id,
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        dto: Optional[UserModel] = result.scalars().one_or_none()

        if not dto:
            return None

        return UserEntity(
            id=dto.id,
            account=dto.account,
            hashed_password=dto.password,
        )

    async def create_user(
            self,
            account: str,
            password: str,
    ) -> int:
        stmt = insert(self.account_model).values(
            account=account,
            password=password,
        )

        try:
            result = await self.db_manager.execute_stmt(stmt=stmt)

        except IntegrityError:
            raise DuplicateAccountException

        inserted_primary_key = result.inserted_primary_key[0]

        return inserted_primary_key
