"""user repo interface"""
import abc
from typing import Optional

from src.entities import UserEntity


class UserRepoInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user_by_account(
            self,
            account: str,
    ) -> Optional[UserEntity]:
        return NotImplemented

    @abc.abstractmethod
    def get_user_by_id(
            self,
            user_id: int,
    ) -> Optional[UserEntity]:
        return NotImplemented

    @abc.abstractmethod
    def create_user(
            self,
            account: str,
            password: str,
    ) -> int:
        return NotImplemented

