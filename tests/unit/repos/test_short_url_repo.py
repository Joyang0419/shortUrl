from typing import Optional

import pytest

from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.entities import ShortUrlEntity
from src.repos import ORMShortUrlsRepo


@pytest.mark.asyncio
class TestShortUrlRepo:

    @pytest.fixture(scope='class')
    async def fake_short_url_repo(self, fake_db_manager: AsyncORMDBManager) \
            -> ORMShortUrlsRepo:
        yield ORMShortUrlsRepo(db_manager=fake_db_manager)

    async def test_create_short_url(self, fake_short_url_repo: ORMShortUrlsRepo):
        data = await fake_short_url_repo.create_short_url(
            user_id=1,
            short_url="",
            target_url="https://www.youtube.com/watch?v=PJJhHihvDpo"
        )

        assert isinstance(data, int)

    async def test_update_target_url(
            self, fake_short_url_repo: ORMShortUrlsRepo
    ):
        data: bool = await fake_short_url_repo.update_target_url(
            user_id=1,
            short_url="",
            modified_target_url="https://www."
                                "osgeo.cn/sqlalchemy/core/defaults.html"
        )

        assert data

    async def test_update_short_url(
            self,
            fake_short_url_repo: ORMShortUrlsRepo
    ):
        data: bool = await fake_short_url_repo.update_short_url(
            short_url_id=1,
            modified_short_url="",
        )

        assert data

    async def test_get_short_url(
            self,
            fake_short_url_repo: ORMShortUrlsRepo
    ):
        data: Optional[ShortUrlEntity] = await \
            fake_short_url_repo.get_short_url(
                short_url=""
            )

        if data is not None:
            assert isinstance(data, ShortUrlEntity)

    async def test_delete_short_urls(
            self,
            fake_short_url_repo: ORMShortUrlsRepo
    ):
        data = await fake_short_url_repo.delete_short_urls(
            user_id=1,
            short_urls=[""]
        )
        assert isinstance(data, bool)
