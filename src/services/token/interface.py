"""json web token services interface"""

import abc
from src.services.token.models import AccessToken

from src.services.token.models import JWTPayload


class TokenInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_access_token(
            self,
            user_id: int,
    ) -> AccessToken:
        return NotImplemented

    @abc.abstractmethod
    def decode_access_token(self, token: str) -> JWTPayload:
        """return JWT payload"""
        return NotImplemented
