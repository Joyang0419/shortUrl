"""user services interface"""

import abc
from typing import Optional, List

from src.entities import UserEntity


class UserServiceInterface(abc.ABC):

    @abc.abstractmethod
    def create_user(
            self,
            account: str,
            password: str,
    ) -> int:
        return NotImplemented

    @abc.abstractmethod
    def get_user_by_account(self, account: str) -> Optional[UserEntity]:
        return NotImplemented

    @abc.abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[UserEntity]:
        return NotImplemented

    @abc.abstractmethod
    def create_token(self, user_id: int) -> str:
        return NotImplemented

    @abc.abstractmethod
    def verify_token(self, token: str) -> bool:
        return NotImplemented
