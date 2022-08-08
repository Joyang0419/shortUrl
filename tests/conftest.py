import asyncio
import os
import typing
from pathlib import Path

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.orm_models.base import BASE
from tests.unit.fake_data import fake_data


class FakeAsyncORMDBManager(AsyncORMDBManager):

    def __init__(self, async_engine: AsyncEngine):
        super().__init__(async_engine)

    async def setup_fake_database(self, fake_data: typing.List[BASE]):
        async with self.async_engine.begin() as conn:
            BASE.metadata.bind = self.async_engine
            await conn.run_sync(BASE.metadata.create_all)

        async with self.get_db() as session:
            async with session.begin():
                session.add_all(fake_data)

    async def drop_all_table(self):
        async with self.async_engine.begin() as conn:
            BASE.metadata.bind = self.async_engine
            await conn.run_sync(BASE.metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop() -> typing.Generator:
    """
    Create an instance of the default event loop for each test case.
    References: https://github.com/pytest-dev/pytest-asyncio/issues/207
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def fake_db_manager() -> FakeAsyncORMDBManager:
    """
    setup and teardown fake database.
    """
    database_filename = 'TestDatabase'
    file_path = Path(__file__).resolve().parent.joinpath(
        database_filename
    )
    fake_db_manager = FakeAsyncORMDBManager(
        async_engine=create_async_engine(
            url='{db_dialect}+{db_driver}:///{file_path}'.format(
                db_dialect='sqlite',
                db_driver='aiosqlite',
                file_path=file_path
            ),
            echo=False,
            future=True
        )
    )
    await fake_db_manager.drop_all_table()
    await fake_db_manager.setup_fake_database(fake_data=fake_data)
    yield fake_db_manager
    await fake_db_manager.drop_all_table()

    if os.path.exists(file_path):
        os.remove(file_path)
