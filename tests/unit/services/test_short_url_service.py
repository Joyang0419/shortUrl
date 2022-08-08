import pytest
from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.services import ShortUrlService
from src.repos import ORMShortUrlsRepo
from src.entities import UserEntity, ShortUrlEntity


@pytest.mark.asyncio
class TestShortUrlService:

    @pytest.fixture(scope='class')
    async def fake_short_url_service(
            self,
            fake_db_manager: AsyncORMDBManager
    ) -> ShortUrlService:

        yield ShortUrlService(
            short_url_repo=ORMShortUrlsRepo(db_manager=fake_db_manager)
        )

    async def test_create_short_url(
            self,
            fake_short_url_service: ShortUrlService
    ):
        data = await fake_short_url_service.create_short_url(
            user_id=1,
            short_url="",
            target_url="https://www.youtube.com/watch?v=PJJhHihvDpo"
        )

        assert isinstance(data, int)

    async def test_get_short_urls(
            self,
            fake_short_url_service: ShortUrlService
    ):
        data = await fake_short_url_service.get_short_urls(user_id=1)

        assert isinstance(data, list)

    async def test_get_short_url(
            self,
            fake_short_url_service: ShortUrlService
    ):
        data = await fake_short_url_service.get_short_url(
            short_url=""
        )

        if data is not None:
            assert isinstance(data, ShortUrlEntity)

    async def test_delete_short_urls(
            self,
            fake_short_url_service: ShortUrlService
    ):
        data = await fake_short_url_service.delete_short_urls(
            user_id=1,
            short_urls=[""]
        )

        assert isinstance(data, bool)

