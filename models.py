from datetime import date
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    wallet: Optional[float] = 0.0
    birthdate: date
