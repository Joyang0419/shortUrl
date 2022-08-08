"""router: short_url request"""

from pydantic import BaseModel, AnyHttpUrl


class CreateShortUrlForm(BaseModel):
    target_url: AnyHttpUrl

    class Config:
        schema_extra = {
            "example": {
                "target_url": "https://www.google.com/",
            }
        }


class ModifyTargetUrlForm(CreateShortUrlForm):

    class Config:
        schema_extra = {
            "example": {
                "target_url": "https://www.google.com/",
            }
        }
