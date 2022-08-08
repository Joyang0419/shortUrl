"""encrypt services interface"""

import abc


class EncryptInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def verify_password(
            self,
            plain_password: str,
            hashed_password: str
    ) -> bool:
        return NotImplemented

    @abc.abstractmethod
    def get_hashed_password(self, plain_password: str) -> str:
        return NotImplemented
