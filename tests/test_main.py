import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app

client = TestClient(app)

def test_root_status_success():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("status") == "success"

def test_root_keys_present():
    data = client.get("/").json()
    # Verifica que as chaves obrigatórias estão presentes
    for key in ("status", "api", "version", "author", "message"):
        assert key in data

def test_root_message_contains_visualiza():
    message = client.get("/").json().get("message", "")
    assert "Visualiza" in message

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

@pytest.mark.asyncio
@patch("src.main.httpx.AsyncClient.get")
async def test_apod_success(mock_get):
    mock_data = {
        "title": "Mock Title",
        "explanation": "Mock explanation",
        "url": "http://example.com/image.jpg"
    }
    class MockResp:
        status_code = 200
        def json(self): return mock_data
        def raise_for_status(self): pass

    mock_get.return_value = MockResp()
    result = await app.router.routes[2].endpoint()
    assert result == mock_data

