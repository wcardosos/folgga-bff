from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)

def test_welcome():
    response = client.get("/")

    assert response.status_code == 200
    assert response.text == '"Welcome to folgga API!"'
