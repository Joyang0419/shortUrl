import pytest

from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.entities import UserEntity
from src.repos import ORMUserRepo


@pytest.mark.asyncio
class TestUserRepo:

    @pytest.fixture(scope='class')
    async def fake_orm_user_repo(self, fake_db_manager: AsyncORMDBManager) \
            -> ORMUserRepo:
        yield ORMUserRepo(db_manager=fake_db_manager)

    async def test_get_user_by_account(self, fake_orm_user_repo: ORMUserRepo):
        data = await fake_orm_user_repo.get_user_by_account(
            account="root"
        )

        if data is not None:
            assert isinstance(data, UserEntity)

    async def test_get_user_by_id(self, fake_orm_user_repo: ORMUserRepo):
        data = await fake_orm_user_repo.get_user_by_id(
            user_id=1
        )

        if data is not None:
            assert isinstance(data, UserEntity)

    async def test_create_user(
            self,
            fake_orm_user_repo: ORMUserRepo
    ):
        data = await fake_orm_user_repo.create_user(
            account="fake",
            password="fake"
        )

        assert isinstance(data, int)
