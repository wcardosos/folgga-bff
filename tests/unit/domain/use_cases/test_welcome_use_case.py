from src.domain.use_cases.welcome_use_case import WelcomeUseCase


def test_execute():
    sut = WelcomeUseCase()

    result = sut.execute()

    assert result == "Welcome to folgga API!"