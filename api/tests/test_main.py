from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "Hello from FastAPI" in r.json()["message"]

def test_create_item():
    payload = {"name":"foo","value":5}
    r = client.post("/items", json=payload)
    assert r.status_code == 200
    assert r.json()["received"]["name"] == "foo"
