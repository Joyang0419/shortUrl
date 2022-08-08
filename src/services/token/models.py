"""json web token services response models."""

from datetime import datetime, timezone

from pydantic import BaseModel

from src.configs.project_config import PermissionsInfo

PERMISSIONS_CONFIG = PermissionsInfo()


class PayloadSub(BaseModel):
    user_id: int


class JWTPayload(BaseModel):
    sub: PayloadSub
    exp: int = \
        int(datetime.now(timezone.utc).timestamp()) + PERMISSIONS_CONFIG.exp

    class Config:
        schema_extra = {
            "example": {
                "sub": {
                    "user_id": "55",
                },
                "exp": 1631774732,
            }
        }


class AccessToken(BaseModel):
    access_token: str
    token_type: str = 'bearer'

    class Config:
        schema_extra = {
            "example": {
                "token": "eyJ0eXAiOiJKV1QiLC...",
                "token_type": "bearer"
            }
        }
