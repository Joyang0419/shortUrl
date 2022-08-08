"""encrypt services implement"""

from passlib.context import CryptContext

from src.services.encrypt.interface import EncryptInterface


class CryptContextEncryptService(EncryptInterface):

    def __init__(self, crypt_context: CryptContext):
        self.crypt_context = crypt_context

    def verify_password(
            self,
            plain_password: str,
            hashed_password: str
    ) -> bool:
        return self.crypt_context.verify(
            secret=plain_password,
            hash=hashed_password
        )

    def get_hashed_password(self, plain_password: str) -> str:
        return self.crypt_context.hash(secret=plain_password)
