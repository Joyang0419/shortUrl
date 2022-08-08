"""Table Schema: user"""

from sqlalchemy import Column, TIMESTAMP, Integer, text
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.sql import func

from src.orm_models.base import BASE


class UserModel(BASE):
    __tablename__ = 'account'
    __table_args__ = {'comment': '帳號資訊'}

    id = Column(
        BIGINT(20).with_variant(Integer, "sqlite"),
        primary_key=True, comment='ID', autoincrement=True
    )
    account = Column(
        VARCHAR(100), nullable=False, unique=True, comment='user user'
    )
    password = Column(
        VARCHAR(100), nullable=False, comment='user password'
    )
    create_time = Column(
        TIMESTAMP, nullable=False,
        server_default=func.now(),
        comment='建立時間'
    )
    update_time = Column(
        TIMESTAMP, nullable=False,
        server_default=func.now(),
        onupdate=func.utc_timestamp(),
        comment='修改時間'
    )

