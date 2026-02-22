import requests
import json

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    data = response.json()
    print(json.dumps(data, indent=4))
    assert response.status_code == 200
    assert "data" in data
    assert data["data"]["id"] == 2
