from typing import List, Optional
from datetime import datetime

from src.domain.models.holiday_response import HolidayResponse
from src.domain.models.holiday import Holiday


class GetNextHolidaysUseCase:
    HOLIDAYS_QUANTITY_DEFAULT = 3

    def execute(
            self,
            holidays: List[HolidayResponse],
            current_date: datetime,
            holidays_quantity: Optional[int] = HOLIDAYS_QUANTITY_DEFAULT
    ) -> List[Holiday]:
        next_holidays = []

        for holiday in holidays:
            if holiday.date > current_date:
                holiday_params = {
                    "date": holiday.date,
                    "name": holiday.name
                }
                next_holidays.append(Holiday(**holiday_params))

            if len(next_holidays) == holidays_quantity:
                break

        return next_holidays

    def _format_date(self, date: str) -> datetime:
        return datetime.strptime(date, "%Y-%m-%d")