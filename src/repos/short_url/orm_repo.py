"""ORM short_url repo implement"""

from typing import List, Optional

from sqlalchemy import insert, update
from sqlalchemy.future import select

from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.entities.short_url_entity import ShortUrlEntity
from src.orm_models.short_url import ShortUrlModel
from src.repos.short_url.interface import ShortUrlsRepoInterface


class ORMShortUrlsRepo(ShortUrlsRepoInterface):
    short_url_model = ShortUrlModel

    def __init__(self, db_manager: AsyncORMDBManager):
        self.db_manager = db_manager

    async def create_short_url(
            self,
            user_id: int,
            short_url: str,
            target_url: str
    ) -> int:
        stmt = insert(self.short_url_model).values(
            user_id=user_id,
            short_url=short_url,
            target_url=target_url
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        inserted_primary_key = result.inserted_primary_key[0]

        return inserted_primary_key

    async def update_target_url(
            self,
            user_id: int,
            short_url: str,
            modified_target_url: str
    ) -> bool:
        stmt = update(self.short_url_model).where(
            self.short_url_model.user_id == user_id,
            self.short_url_model.short_url == short_url
        ).values(
            target_url=modified_target_url
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        if result.rowcount == 0:
            return False

        return True

    async def update_short_url(
            self,
            short_url_id: int,
            modified_short_url: str
    ) -> bool:
        stmt = update(self.short_url_model).where(
            self.short_url_model.id == short_url_id,
        ).values(
            short_url=modified_short_url
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        if result.rowcount == 0:
            return False

        return True

    async def delete_short_urls(self, user_id: int, short_urls: List[str]) \
            -> bool:
        stmt = self.short_url_model.__table__.delete().where(
            self.short_url_model.short_url.in_(short_urls),
            self.short_url_model.user_id == user_id
        )

        await self.db_manager.execute_stmt(stmt=stmt)

        return True

    async def get_short_urls(self, user_id: int) -> List[ShortUrlEntity]:
        stmt = select(self.short_url_model).where(
            self.short_url_model.user_id == user_id,
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        rows = result.fetchall()

        return [
            ShortUrlEntity(
                id=each[0].id,
                user_id=each[0].user_id,
                short_url=each[0].short_url,
                target_url=each[0].target_url,
                create_time=each[0].create_time,
                update_time=each[0].update_time
            )
            for each in rows
        ]

    async def get_short_url(
            self,
            short_url: str
    ) -> Optional[ShortUrlEntity]:
        stmt = select(self.short_url_model).where(
            self.short_url_model.short_url == short_url
        )

        result = await self.db_manager.execute_stmt(stmt=stmt)

        dto: Optional[ShortUrlEntity] = result.scalars().one_or_none()

        if not dto:
            return None

        return ShortUrlEntity(
            id=dto.id,
            user_id=dto.user_id,
            short_url=dto.short_url,
            target_url=dto.target_url,
            create_time=dto.create_time,
            update_time=dto.update_time
        )

