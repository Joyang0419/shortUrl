"""short_url repo interface"""
import abc
from typing import List, Optional

from src.entities import ShortUrlEntity


class ShortUrlsRepoInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def get_short_urls(
            self,
            user_id: int
    ) -> List[ShortUrlEntity]:
        return NotImplemented

    @abc.abstractmethod
    async def create_short_url(
            self,
            user_id: int,
            short_url: str,
            target_url: str,
    ) -> int:
        return NotImplemented

    @abc.abstractmethod
    async def update_target_url(
            self,
            user_id: int,
            short_url: str,
            modified_target_url: str
    ) -> bool:
        return NotImplemented

    @abc.abstractmethod
    async def update_short_url(
            self,
            short_url_id: int,
            modified_short_url: str
    ) -> bool:
        return NotImplemented

    @abc.abstractmethod
    async def delete_short_urls(
            self,
            user_id: int,
            short_urls: List[str]
    ) -> bool:
        return NotImplemented

    @abc.abstractmethod
    async def get_short_url(
            self,
            short_url: str
    ) -> Optional[ShortUrlEntity]:
        return NotImplemented
