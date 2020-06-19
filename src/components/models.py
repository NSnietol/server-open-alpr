from pydantic import BaseModel
from typing import List, Optional


class ResponseAlpr(BaseModel):
    message: Optional[str] = None
    code: Optional[int] = None
    plates: List[str] = []
