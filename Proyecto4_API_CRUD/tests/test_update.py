import requests
import json

BASE_URL = "https://reqres.in/api"

def test_update_user():
    payload = {"name": "Juan", "job": "Senior QA"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert response.status_code == 200
    assert data["job"] == "Senior QA"
