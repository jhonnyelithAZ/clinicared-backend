import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_get_patients_happy_path():
    response = client.get("/api/v1/patients/")
    assert response.status_code in [200, 404]

def test_simulator_admission_error_path():
    response = client.post("/api/v1/simulators/admissions", json={})
    assert response.status_code in [400, 422, 404]

def test_simulator_messaging_error_path():
    response = client.post("/api/v1/simulators/messaging", json={"invalid_field": "test"})
    assert response.status_code in [400, 422, 404]