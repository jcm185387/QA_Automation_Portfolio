import requests, json

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    print("Status:", response.status_code)
    print("Content:", response.text)
    assert response.status_code == 200, f"Esperaba 200 pero recibí {response.status_code}"
    try:
        data = response.json()
        assert data["id"] == 1
    except ValueError:
        assert False, "Respuesta no contenía JSON válido"
