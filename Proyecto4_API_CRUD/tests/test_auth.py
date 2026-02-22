import requests
import json

BASE_URL = "https://reqres.in/api"

def test_login_success():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert response.status_code == 200
    assert "token" in data

def test_login_failure():
    payload = {"email": "peter@klaven"}  # sin password
    response = requests.post(f"{BASE_URL}/login", json=payload)
    data = response.json()
    print(json.dumps(data, indent=4))
    assert response.status_code == 400
    assert "error" in data
