from datetime import datetime
from typing import List

from src.domain.clients.holidays_client import HolidaysClient
from src.domain.models.holiday import Holiday


class FetchHolidaysUseCase:
    def __init__(self, holidays_client: HolidaysClient):
        self.holidays_client = holidays_client

    def execute(self) -> List[Holiday]:
        now = datetime.now()
        holidays = self.holidays_client.fetch_holidays(now.year)

        return holidays