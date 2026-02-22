import requests, json

BASE_URL = "https://reqres.in/api"

def test_create_user():
    payload = {"name": "Juan", "job": "QA Automation"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    print("Status:", response.status_code)
    print("Content:", response.text)
    assert response.status_code == 201, f"Esperaba 201 pero recibí {response.status_code}"
    try:
        data = response.json()
        assert "id" in data
    except ValueError:
        assert False, "Respuesta no contenía JSON válido"
