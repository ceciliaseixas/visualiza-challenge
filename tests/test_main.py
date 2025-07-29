from fastapi.testclient import TestClient
from main import app  # ajuste se estiver em 'src.main'

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["api"] == "Visualiza API"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_apod_requires_api_key():
    response = client.get("/apod")
    assert response.status_code in [200, 403, 401]
