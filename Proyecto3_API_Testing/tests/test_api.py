import requests

def test_get_posts_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

def test_get_posts_json_structure():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    assert isinstance(data, list)
    assert "userId" in data[0]
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]

def test_get_single_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)


def test_get_invalid_post_returns_404(): 
    response = requests.get("https://jsonplaceholder.typicode.com/posts/999999") 
    assert response.status_code == 404
