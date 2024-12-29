import datetime

from fastapi import FastAPI

from src.domain.use_cases.fetch_holidays_use_case import FetchHolidaysUseCase
from src.domain.use_cases.get_next_holidays_use_case import GetNextHolidaysUseCase
from src.domain.use_cases.welcome_use_case import WelcomeUseCase
from src.infra.clients.requests_holidays_client import RequestsHolidaysClient
from src.infra.providers.http_adapter import HttpAdapter

app = FastAPI()


@app.get("/")
def get_root():
    welcome_use_case = WelcomeUseCase()
    return welcome_use_case.execute()

@app.get("/holidays/next")
def get_next_holidays():
    http_adapter = HttpAdapter()
    holidays_client = RequestsHolidaysClient(http_adapter)
    fetch_holidays_use_case = FetchHolidaysUseCase(holidays_client)
    get_next_holidays_use_case = GetNextHolidaysUseCase()

    holidays = fetch_holidays_use_case.execute()

    next_holidays = get_next_holidays_use_case.execute(holidays, datetime.datetime.now())

    return next_holidays

