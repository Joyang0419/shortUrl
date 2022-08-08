from pydantic import BaseModel


class TokenEntity(BaseModel):
    id: int
    user_id: int
    token: str
