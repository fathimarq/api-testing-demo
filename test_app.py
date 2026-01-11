from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add_item():
    response = client.post("/items", params={"name": "Keploy"})
    assert response.status_code == 200
    assert response.json() == {"name": "Keploy", "status": "added"}

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert "Keploy" in response.json()
