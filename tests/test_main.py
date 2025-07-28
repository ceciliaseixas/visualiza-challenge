import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_root_response_format():
    response = client.get("/")
    assert isinstance(response.json(), dict)
    assert "status" in response.json()
    assert "api" in response.json()
    assert "version" in response.json()
    assert "author" in response.json()
    assert "message" in response.json()

def test_root_message_content():
    response = client.get("/")
    message = response.json().get("message", "")
    assert "Visualiza" in message
