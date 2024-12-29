from pydantic import BaseModel
from datetime import datetime


class HolidayResponse(BaseModel):
    date: datetime
    name: str
    type: str
