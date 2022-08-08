import pytest
from src.db_manager.async_orm_db_manager import AsyncORMDBManager
from src.services import UserService
from src.repos import ORMUserRepo
from src.entities import UserEntity


@pytest.mark.asyncio
class TestAccountService:

    @pytest.fixture(scope='class')
    async def fake_user_service(
            self,
            fake_db_manager: AsyncORMDBManager
    ) -> UserService:

        yield UserService(user_repo=ORMUserRepo(db_manager=fake_db_manager))

    async def test_get_user_by_account(self, fake_user_service: UserService):
        data = await fake_user_service.get_user_by_account(account="root")

        if data is not None:
            assert isinstance(data, UserEntity)

    async def test_get_user_by_id(self, fake_user_service: UserService):
        data = await fake_user_service.get_user_by_id(user_id=1)

        if data is not None:
            assert isinstance(data, UserEntity)

    async def test_create_user(self, fake_user_service: UserService):
        data = await fake_user_service.create_user(
            account="Joy",
            password="Joy"
        )

        assert isinstance(data, int)

