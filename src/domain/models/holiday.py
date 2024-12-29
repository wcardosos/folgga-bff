from pydantic import BaseModel

from datetime import datetime


class Holiday(BaseModel):
    date: datetime
    name: str
