import logging
import sys
from pathlib import Path

from starlette.config import Config

CONFIG = Config(
    env_file=Path(__file__).resolve().parent.parent.parent.joinpath(".env"))

VERSION_CONFIG = Config(
    env_file=Path(__file__).resolve().parent.parent.parent.joinpath("VERSION")
)

PROJECT_NAME: str = CONFIG(
    "PROJECT_NAME",
    default="ShortUrl"
)

VERSION = VERSION_CONFIG("VERSION", default="v0.0.0")

DEBUG: bool = CONFIG("DEBUG", cast=bool, default=False)

LOGURU_HANDLERS = [
    {
        "sink": sys.stdout,
        "level": logging.DEBUG if DEBUG else logging.INFO
    }
]

JWT_ALGORITHM = "RS256"

with open(
        Path(__file__).resolve().parent.parent.parent.joinpath("jwtRS256.key"),
        'r') as f:
    PRIVATE_KEY = f.read()

with open(Path(__file__).resolve().parent.parent.parent.joinpath(
        "jwtRS256.key.pub"), 'r') as f:
    PUBLIC_KEY = f.read()
