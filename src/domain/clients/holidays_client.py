from abc import ABC, abstractmethod
from typing import List

from src.domain.models.holiday_response import HolidayResponse
from src.domain.providers.http_provider import HttpProvider


class HolidaysClient(ABC):
    def __init__(self, http_provider: HttpProvider):
        self.http_provider = http_provider

    @abstractmethod
    def fetch_holidays(self, year) -> List[HolidayResponse]:
        pass