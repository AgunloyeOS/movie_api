from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_comment():
    client.post("/register", json={"email": "testuser@example.com", "password": "password123"})
    response = client.post("/login", data={"username": "testuser@example.com", "password": "password123"})
    token = response.json()["access_token"]

    response = client.post("/movies", json={"title": "Living in Bondage", "description": "Nigerian thriller"},
                            headers={"Authorization": f"Bearer {token}"})
    movie_id = response.json()["id"]

    response = client.post(f"/movies/{movie_id}/comments", json={"content": "This movie is thrilling!"},
                            headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
