import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from fastapi_app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Ilya", "email": "Ilya@example.com", "wage": 200})
    assert response.status_code == 200
    assert response.json()["name"] == "Ilya"
    assert response.json()["email"] == "Ilya@example.com"
    assert response.json()["wage"] == 200

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
