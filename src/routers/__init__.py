from pydantic import BaseModel
from typing import Optional, Any


class FormatResponse(BaseModel):
    data: Optional[Any]
    error_message: Optional[str]
