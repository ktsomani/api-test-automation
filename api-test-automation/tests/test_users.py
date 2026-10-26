import requests

from config import BASE_URL, TIMEOUT


def test_list_users_returns_10():
    r = requests.get(f"{BASE_URL}/users", timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) == 10


def test_user_has_required_fields():
    r = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)
    body = r.json()
    for field in ("id", "name", "username", "email"):
        assert field in body


def test_user_email_format():
    body = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT).json()
    assert "@" in body["email"]


def test_unknown_user_returns_404():
    r = requests.get(f"{BASE_URL}/users/999999", timeout=TIMEOUT)
    assert r.status_code == 404


def test_non_numeric_user_id_returns_404():
    r = requests.get(f"{BASE_URL}/users/abc", timeout=TIMEOUT)
    assert r.status_code == 404


def test_create_user_returns_201_or_200():
    payload = {"name": "QA Tester", "username": "qa", "email": "qa@example.com"}
    r = requests.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT)
    assert r.status_code in (200, 201)
    assert r.json()["name"] == "QA Tester"
