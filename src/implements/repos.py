"""repos implements"""
from src.implements.db_manager import ASYNC_SQLALCHEMY
from src.repos import ORMUserRepo, ORMShortUrlsRepo

USER_REPO = ORMUserRepo(db_manager=ASYNC_SQLALCHEMY)
SHORT_URL_REPO = ORMShortUrlsRepo(db_manager=ASYNC_SQLALCHEMY)
