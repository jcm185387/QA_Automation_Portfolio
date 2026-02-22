import requests, json

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    print("Status:", response.status_code)
    print("Content:", response.text)
    assert response.status_code == 200, f"Esperaba 200 pero recibí {response.status_code}"
    try:
        data = response.json()
        assert "data" in data
        assert data["data"]["id"] == 2
    except ValueError:
        assert False, "Respuesta no contenía JSON válido"
