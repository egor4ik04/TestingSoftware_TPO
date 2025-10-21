import requests

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"
HEADERS = {"x-api-key": API_KEY}


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS, timeout=5)
    assert response.status_code == 200, "Ожидался статус 200"
    data = response.json()
    assert "data" in data, "В ответе нет объекта data"
    assert "email" in data["data"], "Нет поля email"
    assert "@" in data["data"]["email"], "Неверный формат email"
    assert data["data"]["id"] == 2, "ID пользователя не равен 2"


def test_create_user():
    payload = {"name": "Egor", "job": "Tester"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS, timeout=5)
    assert response.status_code == 201, "Ожидался статус 201"
    data = response.json()
    assert data["name"] == "Egor", "Имя не совпадает"
    assert data["job"] == "Tester", "Профессия не совпадает"
    assert "id" in data, "Нет поля id"
    assert "createdAt" in data, "Нет поля createdAt"


def test_update_user():
    payload = {"name": "Egor", "job": "Toster"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS, timeout=5)
    assert response.status_code == 200, "Ожидался статус 200"
    data = response.json()
    assert data["name"] == "Egor", "Имя не совпадает"
    assert data["job"] == "Toster", "Профессия не обновилась"
    assert "updatedAt" in data, "Нет поля updatedAt"
