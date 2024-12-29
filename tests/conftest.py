import pytest

from constants import holidays_2024, holidays_2025


@pytest.fixture
def api_holidays_2024():
    return holidays_2024

@pytest.fixture
def api_holidays_2024_and_2025():
    return holidays_2024 + holidays_2025