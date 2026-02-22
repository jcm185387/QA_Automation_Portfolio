import requests

BASE_URL = "https://reqres.in/api"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    print("Status:", response.status_code)
    print("Content:", response.text)
    assert response.status_code == 204, f"Esperaba 204 pero recibí {response.status_code}"
