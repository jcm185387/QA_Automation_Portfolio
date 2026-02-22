import requests
import json

BASE_URL = "https://reqres.in/api"

def test_create_user():
    payload = {"name": "Juan", "job": "QA Automation"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert response.status_code == 201
    assert data["name"] == "Juan"
    assert data["job"] == "QA Automation"
