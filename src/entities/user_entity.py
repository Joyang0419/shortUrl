from pydantic import BaseModel


class UserEntity(BaseModel):
    id: int
    account: str
    hashed_password: str
