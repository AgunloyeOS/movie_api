from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_movie():
    client.post("/register", json={"email": "testuser@example.com", "password": "password123"})
    response = client.post("/login", data={"username": "testuser@example.com", "password": "password123"})
    token = response.json()["access_token"]

    response = client.post("/movies", json={"title": "The Wedding Party", "description": "Nigerian comedy-drama"},
                            headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["title"] == "The Wedding Party"
