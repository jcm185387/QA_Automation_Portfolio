import requests, json

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_update_user():
    payload = {"name": "Juan", "job": "Senior QA"}
    response = requests.put(f"{BASE_URL}/users/1", json=payload)
    print("Status:", response.status_code)
    print("Content:", response.text)
    assert response.status_code == 200, f"Esperaba 200 pero recibí {response.status_code}"
    try:
        data = response.json()
        assert data["job"] == "Senior QA"
    except ValueError:
        assert False, "Respuesta no contenía JSON válido"
