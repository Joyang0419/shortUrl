"""json web token services implement"""

import jwt
from jwt import ExpiredSignatureError

from src.services.token.exceptions import DecodeException
from src.services.token.interface import TokenInterface
from src.services.token.models import JWTPayload, PayloadSub, AccessToken


class JsonWebTokenService(TokenInterface):

    def __init__(
            self,
            private_key: str,
            public_key: str,
            algorithm: str
    ):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def create_access_token(
            self,
            user_id: int,
    ) -> AccessToken:
        jwt_payload = JWTPayload(
            sub=PayloadSub(
                user_id=user_id,
            )
        )

        token = jwt.encode(
            payload=jwt_payload.dict(),
            key=self.private_key,
            algorithm=self.algorithm
        )

        return AccessToken(
            access_token=token
        )

    def decode_access_token(self, token: str) -> JWTPayload:
        """return JWT payload"""
        try:
            decode_token = jwt.decode(
                jwt=token,
                key=self.public_key,
                algorithms=[self.algorithm]
            )

        except (jwt.DecodeError, ExpiredSignatureError):
            raise DecodeException

        return JWTPayload(**decode_token)
