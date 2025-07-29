import pytest
from fastapi.testclient import TestClient
from src.main import app  # Agora importa direto de main.py, não de src.main

from unittest.mock import patch

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()
    assert response.json()["status"] == "success"

def test_root_response_format():
    response = client.get("/")
    body = response.json()
    assert isinstance(body, dict)
    assert "status" in body
    assert "api" in body
    assert "version" in body
    assert "author" in body
    assert "message" in body

def test_root_message_content():
    response = client.get("/")
    message = response.json().get("message", "")
    assert "Visualiza" in message

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch("main.httpx.AsyncClient.get")  # <- Aqui o patch mudou!
@pytest.mark.asyncio
async def test_apod_success(mock_get):
    # Simula a resposta da API da NASA
    mock_data = {
        "title": "Test APOD",
        "explanation": "Example",
        "url": "http://example.com/image.jpg"
    }
    class MockResponse:
        def __init__(self):
            self.status_code = 200
        def json(self):
            return mock_data
        def raise_for_status(self):
            pass
    mock_get.return_value = MockResponse()
    
    # Faz a chamada async usando o TestClient
    # TestClient não suporta await direto, então você pode testar como função separada
    from main import get_apod
    result = await get_apod()
    assert result == mock_data
