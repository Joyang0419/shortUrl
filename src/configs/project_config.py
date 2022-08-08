"""Configurations for this project.
"""

import json
from json.decoder import JSONDecodeError
from pathlib import Path

from pydantic import BaseSettings


def capable_of_parsing_list_with_comma(value):
    """Adds capable of parsing list with comma.
    Example:
        Input: "example1.com:9200,example2.com:9200"
        Output: ["example1.com:9200", "example2.com:9200]
    """

    try:
        return json.loads(value)

    except JSONDecodeError:
        return value.split(",")


class Settings(BaseSettings):
    """Pydantic Base Settings"""

    class Config:
        env_file = Path(
            __file__).resolve().parent.parent.parent.joinpath(".env")
        json_loads = capable_of_parsing_list_with_comma


class DatabaseConfig(Settings):
    """Database Config"""
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PWD: str = "root"
    DB_NAME: str = "metropia"
    CONNECTION_TIMEOUT: int = 5


class DatabaseConnectionConfig(Settings):
    """Database Connection Settings"""

    DB_CONNECTION_MINCACHED: int = 3
    DB_CONNECTION_MAXCACHED: int = 5
    DB_CONNECTION_MAXCONNECTIONS: int = 10


class PermissionsInfo(Settings):
    exp = 60 * 60 * 24 * 365
