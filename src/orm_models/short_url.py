"""Table Schema: short_url"""

from sqlalchemy import Column, String, TIMESTAMP, Integer, text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.sql import func

from src.orm_models.base import BASE


class ShortUrlModel(BASE):
    __tablename__ = 'short_url'
    __table_args__ = {'comment': '短網址表', 'sqlite_autoincrement': True}

    id = Column(
        BIGINT(20).with_variant(Integer, "sqlite"),
        primary_key=True, comment='ID', autoincrement=True
    )
    user_id = Column(
        BIGINT(20), nullable=False, index=True, comment='用戶資訊ID'
    )
    short_url = Column(String(2000), nullable=False, comment='短網址')
    target_url = Column(String(2000), nullable=False, comment='長網址')
    create_time = Column(
        TIMESTAMP, nullable=False,
        server_default=func.now(),
        comment='建立時間'
    )
    from datetime import datetime
    update_time = Column(
        TIMESTAMP, nullable=False,
        default=datetime.utcnow(),
        comment='修改時間'
    )
