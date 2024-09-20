import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"email": "testuser@example.com", "password": "password123"})
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_register_user_with_invalid_email():
    response = client.post("/register", json={"email": "invalid-email", "password": "password123"})
    assert response.status_code == 422
