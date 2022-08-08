"""Async ORM DB Manager implement"""

import contextlib
from typing import Callable, Union

from sqlalchemy.engine import Result, BaseCursorResult
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from src.db_manager.interface import DBManagerInterface


class AsyncORMDBManager(DBManagerInterface):

    def __init__(
            self,
            async_engine: AsyncEngine
    ):
        self.async_engine = async_engine

        async_session_factory = sessionmaker(
            bind=self.async_engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

        self._async_session = async_session_factory()

    @contextlib.asynccontextmanager
    async def get_db(self) -> Callable[..., AsyncSession]:
        """contextmanager will create and teardown a async async_session"""
        try:
            yield self._async_session
            await self._async_session.commit()

        except Exception:
            await self._async_session.rollback()
            raise

        finally:
            await self._async_session.close()

    async def is_connected(self) -> bool:
        try:
            async with self.async_engine.connect():
                return True
        except OperationalError:
            return False

    async def execute_stmt(self, stmt: str) -> Union[Result, BaseCursorResult]:
        async with self.get_db() as session:
            async with session.begin():
                result: Union[Result, BaseCursorResult] = \
                    await session.execute(stmt)
        return result
