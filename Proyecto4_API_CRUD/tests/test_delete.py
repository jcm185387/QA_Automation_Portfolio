import requests

BASE_URL = "https://reqres.in/api"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
