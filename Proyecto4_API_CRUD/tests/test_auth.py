import requests
import json

BASE_URL = "https://reqres.in/api"

def test_login_success():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    print("Status:", response.status_code)
    print("Content:", response.text)

    if response.status_code == 403:
        assert False, f"El endpoint devolvió 403 (Forbidden). Esperaba 200."
    else:
        assert response.status_code == 200, f"Esperaba 200 pero recibí {response.status_code}"
        try:
            data = response.json()
            assert "token" in data, "La respuesta no contiene 'token'"
        except ValueError:
            assert False, "Respuesta no contenía JSON válido"

def test_login_failure():
    payload = {"email": "peter@klaven"}  # sin password
    response = requests.post(f"{BASE_URL}/login", json=payload)
    print("Status:", response.status_code)
    print("Content:", response.text)

    assert response.status_code == 400, f"Esperaba 400 pero recibí {response.status_code}"
    try:
        data = response.json()
        assert "error" in data, "La respuesta no contiene 'error'"
    except ValueError:
        assert False, "Respuesta no contenía JSON válido"
