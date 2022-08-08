"""router: user request"""

from pydantic import BaseModel


class RegisterForm(BaseModel):
    account: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "account": "account",
                "password": "password",
            }
        }


class LoginForm(RegisterForm):
    pass
