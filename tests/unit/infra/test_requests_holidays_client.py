from typing import List
import pytest

from src.domain.exceptions.year_out_of_range_exception import YearOutOfRangeException
from src.domain.models.holiday_response import HolidayResponse
from src.infra.clients.requests_holidays_client import RequestsHolidaysClient
from src.infra.providers.http_adapter import HttpAdapter
from requests import Response


def test_fetch_holidays_successfully(api_holidays_2024: List[HolidayResponse], mocker):
    year_mock = 2024
    http_adapter = HttpAdapter()
    get_http_adapter_spy = mocker.spy(http_adapter, 'get')
    response_mock = Response()
    response_mock.status_code = 200
    response_mock.raw = api_holidays_2024
    get_http_adapter_spy.return_value = response_mock
    sut = RequestsHolidaysClient(http_adapter)

    result = sut.fetch_holidays(year_mock)

    get_http_adapter_spy.assert_called_once_with(sut.BASE_HOLIDAYS_API_URL + str(year_mock))
    assert len(result) == len(api_holidays_2024)

def test_fetch_holidays_with_year_out_of_range_exception(mocker):
    year_mock = 2500
    http_adapter = HttpAdapter()
    get_http_adapter_spy = mocker.spy(http_adapter, 'get')
    response_mock = Response()
    response_mock.status_code = 404
    get_http_adapter_spy.return_value = response_mock
    sut = RequestsHolidaysClient(http_adapter)

    with pytest.raises(YearOutOfRangeException) as result:
        sut.fetch_holidays(year_mock)

    assert str(result.value) == f"The year {year_mock} is out of range"


