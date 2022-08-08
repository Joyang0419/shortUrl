"""DB Manager interface"""

import abc


class DBManagerInterface(abc.ABC):

    @abc.abstractmethod
    def get_db(self):
        return NotImplemented

    @abc.abstractmethod
    def is_connected(self) -> bool:
        return NotImplemented

    @abc.abstractmethod
    def execute_stmt(self, stmt: str):
        return NotImplemented
