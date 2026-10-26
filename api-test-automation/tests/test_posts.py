import requests

from config import BASE_URL, TIMEOUT


def test_list_posts_returns_100():
    r = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) == 100


def test_post_has_required_fields():
    body = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT).json()
    for field in ("userId", "id", "title", "body"):
        assert field in body


def test_filter_posts_by_user():
    r = requests.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT)
    posts = r.json()
    assert posts and all(p["userId"] == 1 for p in posts)


def test_empty_title_is_accepted_documented_defect():
    payload = {"title": "", "body": "x", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)
    # The fake API accepts anything; this test documents current behaviour.
    assert r.status_code == 201


def test_unknown_post_returns_404():
    r = requests.get(f"{BASE_URL}/posts/999999", timeout=TIMEOUT)
    assert r.status_code == 404


def test_update_post_title():
    r = requests.put(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Updated", "body": "b", "userId": 1},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    assert r.json()["title"] == "Updated"
