from datetime import datetime
from typing import List

from src.domain.models.holiday_response import HolidayResponse
from src.domain.models.holiday import Holiday
from src.domain.use_cases.get_next_holidays_use_case import GetNextHolidaysUseCase


SAME_YEAR_DATE_MOCK = datetime.strptime("2024-01-20", "%Y-%m-%d")
ACROSS_YEARS_DATE_MOCK = datetime.strptime("2024-12-23", "%Y-%m-%d")


def test_execute_same_year(api_holidays_2024: List[HolidayResponse]):
    # When the next holidays were in same year
    EXPECTED_NEXT_HOLIDAY_RESPONSES = [
        {
            "date": "2024-02-13",
            "name": "Carnaval",
        },
        {
            "date": "2024-03-29",
            "name": "Sexta-feira Santa",
        },
        {
            "date": "2024-03-31",
            "name": "Páscoa",
        }
    ]
    EXPECTED_NEXT_HOLIDAYS = list(map(lambda holiday : Holiday(**holiday), EXPECTED_NEXT_HOLIDAY_RESPONSES))
    sut = GetNextHolidaysUseCase()

    result = sut.execute(api_holidays_2024, SAME_YEAR_DATE_MOCK)

    assert result == EXPECTED_NEXT_HOLIDAYS

def test_execute_across_years(api_holidays_2024_and_2025: List[HolidayResponse]):
    # When the next holidays were in same year
    EXPECTED_NEXT_HOLIDAY_RESPONSES = [
        {
            "date": "2024-12-25",
            "name": "Natal",
            "type": "national"
        },
        {
            "date": "2025-01-01",
            "name": "Confraternização mundial",
            "type": "national"
        },
        {
            "date": "2025-03-04",
            "name": "Carnaval",
            "type": "national"
        }
    ]
    EXPECTED_NEXT_HOLIDAYS = list(map(lambda holiday: Holiday(**holiday), EXPECTED_NEXT_HOLIDAY_RESPONSES))
    sut = GetNextHolidaysUseCase()

    result = sut.execute(api_holidays_2024_and_2025, ACROSS_YEARS_DATE_MOCK)

    assert result == EXPECTED_NEXT_HOLIDAYS