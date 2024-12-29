from typing import List
from datetime import datetime

from pytest_mock import mocker

from src.domain.models.holiday_response import HolidayResponse
from src.domain.use_cases.fetch_holidays_use_case import FetchHolidaysUseCase
from src.infra.clients.requests_holidays_client import RequestsHolidaysClient
from src.infra.providers.http_adapter import HttpAdapter


def test_fetch_holidays_successfully(api_holidays_2024: List[HolidayResponse], mocker):
    http_adapter = HttpAdapter()
    holidays_client = RequestsHolidaysClient(http_adapter)
    fetch_holidays_holidays_client_spy = mocker.spy(holidays_client, 'fetch_holidays')
    fetch_holidays_holidays_client_spy.return_value = api_holidays_2024
    sut = FetchHolidaysUseCase(holidays_client)

    result = sut.execute()

    fetch_holidays_holidays_client_spy.assert_called_once_with(datetime.now().year)
    assert len(result) == len(api_holidays_2024)