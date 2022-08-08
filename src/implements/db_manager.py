"""DB manager implements"""

from sqlalchemy.ext.asyncio import create_async_engine

from src.configs.project_config import DatabaseConfig
from src.db_manager import AsyncORMDBManager

DATABASE_CONFIG = DatabaseConfig()

SQLALCHEMY_URL = "{db_dialect}+{db_driver}://{db_username}" \
                 ":{db_password}@{db_host}:{db_port}/{db_name}".format(
                    db_dialect='mysql',
                    db_driver='pymysql',
                    db_username=DATABASE_CONFIG.DB_USER,
                    db_password=DATABASE_CONFIG.DB_PWD,
                    db_host=DATABASE_CONFIG.DB_HOST,
                    db_port=DATABASE_CONFIG.DB_PORT,
                    db_name=DATABASE_CONFIG.DB_NAME)

ASYNC_SQLALCHEMY_URL = "{db_dialect}+{db_driver}://{db_username}" \
                 ":{db_password}@{db_host}:{db_port}/{db_name}".format(
                    db_dialect='mysql',
                    db_driver='aiomysql',
                    db_username=DATABASE_CONFIG.DB_USER,
                    db_password=DATABASE_CONFIG.DB_PWD,
                    db_host=DATABASE_CONFIG.DB_HOST,
                    db_port=DATABASE_CONFIG.DB_PORT,
                    db_name=DATABASE_CONFIG.DB_NAME)


ASYNC_SQLALCHEMY = AsyncORMDBManager(
    async_engine=create_async_engine(
        url=ASYNC_SQLALCHEMY_URL,
        echo=False,
        future=True,
        pool_size=5,
        max_overflow=0,
        pool_pre_ping=True,
        pool_recycle=360,
        connect_args={'connect_timeout': 5}
    )
)
