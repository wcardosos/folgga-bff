from src.domain.models.holiday_response import HolidayResponse

holiday_response_mapper = lambda holiday: HolidayResponse(**holiday)

holidays_2024 = list(map(
    holiday_response_mapper,
    [
        {
            "date": "2024-01-01",
            "name": "Confraternização mundial",
            "type": "national"
        },
        {
            "date": "2024-02-13",
            "name": "Carnaval",
            "type": "national"
        },
        {
            "date": "2024-03-29",
            "name": "Sexta-feira Santa",
            "type": "national"
        },
        {
            "date": "2024-03-31",
            "name": "Páscoa",
            "type": "national"
        },
        {
            "date": "2024-04-21",
            "name": "Tiradentes",
            "type": "national"
        },
        {
            "date": "2024-05-01",
            "name": "Dia do trabalho",
            "type": "national"
        },
        {
            "date": "2024-05-30",
            "name": "Corpus Christi",
            "type": "national"
        },
        {
            "date": "2024-09-07",
            "name": "Independência do Brasil",
            "type": "national"
        },
        {
            "date": "2024-10-12",
            "name": "Nossa Senhora Aparecida",
            "type": "national"
        },
        {
            "date": "2024-11-02",
            "name": "Finados",
            "type": "national"
        },
        {
            "date": "2024-11-15",
            "name": "Proclamação da República",
            "type": "national"
        },
        {
            "date": "2024-11-20",
            "name": "Dia da consciência negra",
            "type": "national"
        },
        {
            "date": "2024-12-25",
            "name": "Natal",
            "type": "national"
        }
    ])
)

holidays_2025 = list(map(
    holiday_response_mapper,
    [
        {
            "date": "2025-01-01",
            "name": "Confraternização mundial",
            "type": "national"
        },
        {
            "date": "2025-03-04",
            "name": "Carnaval",
            "type": "national"
        },
        {
            "date": "2025-04-18",
            "name": "Sexta-feira Santa",
            "type": "national"
        },
        {
            "date": "2025-04-20",
            "name": "Páscoa",
            "type": "national"
        },
        {
            "date": "2025-04-21",
            "name": "Tiradentes",
            "type": "national"
        },
        {
            "date": "2025-05-01",
            "name": "Dia do trabalho",
            "type": "national"
        },
        {
            "date": "2025-06-19",
            "name": "Corpus Christi",
            "type": "national"
        },
        {
            "date": "2025-09-07",
            "name": "Independência do Brasil",
            "type": "national"
        },
        {
            "date": "2025-10-12",
            "name": "Nossa Senhora Aparecida",
            "type": "national"
        },
        {
            "date": "2025-11-02",
            "name": "Finados",
            "type": "national"
        },
        {
            "date": "2025-11-15",
            "name": "Proclamação da República",
            "type": "national"
        },
        {
            "date": "2025-11-20",
            "name": "Dia da consciência negra",
            "type": "national"
        },
        {
            "date": "2025-12-25",
            "name": "Natal",
            "type": "national"
        }
    ])
)