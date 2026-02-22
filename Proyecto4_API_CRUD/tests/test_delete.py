import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/1")
    print("Status:", response.status_code)
    print("Content:", response.text)
    assert response.status_code == 200 or response.status_code == 204, \
        f"Esperaba 200/204 pero recibí {response.status_code}"
