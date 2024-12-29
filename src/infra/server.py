from fastapi import FastAPI

from src.domain.use_cases.welcome_use_case import WelcomeUseCase

app = FastAPI()


@app.get("/")
def get_root():
    welcome_use_case = WelcomeUseCase()
    return welcome_use_case.execute()
