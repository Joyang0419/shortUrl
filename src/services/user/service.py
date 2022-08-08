"""user services implement"""

from typing import Optional

from src.entities import UserEntity
from src.repos import ORMUserRepo
from src.repos.user.exceptions import DuplicateAccountException
from src.services.user.exceptions import CreateUserException
from src.services.user.interface import UserServiceInterface


class UserService(UserServiceInterface):

    def __init__(
            self,
            user_repo: ORMUserRepo,
    ):
        self.user_repo = user_repo

    async def create_user(
            self,
            account: str,
            password: str,
    ) -> int:
        try:
            user_id = await self.user_repo.create_user(
                account=account,
                password=password,
            )
        except DuplicateAccountException as e:
            raise CreateUserException(message=e.message)

        return user_id

    async def get_user_by_account(self, account: str) -> Optional[UserEntity]:
        user = await self.user_repo.get_user_by_account(account=account)
        if not user:
            return None

        return user

    async def get_user_by_id(self, user_id: int) -> Optional[UserEntity]:
        user = await self.user_repo.get_user_by_id(user_id=user_id)
        if not user:
            return None

        return user

    def create_token(self, user_id: int) -> str:
        pass

    def verify_token(self, token: str) -> bool:
        pass


