"""short_url services interface"""

import abc
from typing import Optional, List

from src.entities import ShortUrlEntity


class ShortUrlServiceInterface(abc.ABC):

    @abc.abstractmethod
    async def create_short_url(
            self,
            user_id: int,
            short_url: str,
            target_url: str,
    ) -> int:
        return NotImplemented

    @abc.abstractmethod
    async def get_short_urls(self, user_id: int) -> List[ShortUrlEntity]:
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
