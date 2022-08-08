from pydantic import BaseModel
from datetime import datetime


class ShortUrlEntity(BaseModel):
    id: int
    user_id: int
    short_url: str
    target_url: str
    create_time: datetime
    update_time: datetime
