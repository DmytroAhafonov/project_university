import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user_success(client):
    response = client.post('/users', json={
        "name": "Test User",
        "email": "test@example.com"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"

def test_create_user_missing_email(client):
    response = client.post('/users', json={
        "name": "No Email User"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
