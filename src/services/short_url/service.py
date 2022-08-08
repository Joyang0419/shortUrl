"""short_url services implement"""

from typing import Optional, List

from src.entities import ShortUrlEntity
from src.services.short_url.interface import ShortUrlServiceInterface
from src.repos.short_url.interface import ShortUrlsRepoInterface


class ShortUrlService(ShortUrlServiceInterface):

    def __init__(
            self,
            short_url_repo: ShortUrlsRepoInterface,
    ):
        self.short_url_repo = short_url_repo

    async def create_short_url(
            self,
            user_id: int,
            short_url: str,
            target_url: str
    ) -> int:
        short_url_id = await self.short_url_repo.create_short_url(
            user_id=user_id,
            short_url=short_url,
            target_url=target_url
        )

        return short_url_id

    async def get_short_urls(self, user_id: int) -> List[ShortUrlEntity]:
        short_urls = await self.short_url_repo.get_short_urls(user_id=user_id)
        return short_urls

    async def delete_short_urls(self, user_id: int, short_urls: List[str]) \
            -> bool:
        return await self.short_url_repo.delete_short_urls(
            user_id=user_id,
            short_urls=short_urls
        )

    async def update_target_url(self, user_id: int, short_url: str,
                                modified_target_url: str) -> bool:
        return await self.short_url_repo.update_target_url(
            user_id=user_id,
            short_url=short_url,
            modified_target_url=modified_target_url
        )

    async def get_short_url(
            self,
            short_url: str
    ) -> Optional[ShortUrlEntity]:
        return await self.short_url_repo.get_short_url(
            short_url=short_url
        )

    async def update_short_url(
            self,
            short_url_id: int,
            modified_short_url: str
    ) -> bool:
        return await self.short_url_repo.update_short_url(
            short_url_id=short_url_id,
            modified_short_url=modified_short_url
        )
