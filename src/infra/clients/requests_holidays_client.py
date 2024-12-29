from typing import List

from src.domain.clients.holidays_client import HolidaysClient
from src.domain.exceptions.unexpected_error_exception import UnexpectedErrorException
from src.domain.exceptions.year_out_of_range_exception import YearOutOfRangeException
from src.domain.models.holiday_response import HolidayResponse
from src.domain.models.holiday import Holiday


class RequestsHolidaysClient(HolidaysClient):
    BASE_HOLIDAYS_API_URL = "https://brasilapi.com.br/api/feriados/v1/"

    def fetch_holidays(self, year: int) -> List[HolidayResponse]:
        response = self.http_provider.get(self.BASE_HOLIDAYS_API_URL + str(year))

        if response.status_code == 404:
            raise YearOutOfRangeException(year)
        elif response.status_code == 500:
            raise UnexpectedErrorException()

        holidays_response = response.json()

        return list(map(lambda holiday : Holiday(**holiday) , holidays_response))

