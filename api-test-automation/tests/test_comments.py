import requests

from config import BASE_URL, TIMEOUT


def test_comments_for_post_1():
    r = requests.get(f"{BASE_URL}/posts/1/comments", timeout=TIMEOUT)
    assert r.status_code == 200
    assert all(c["postId"] == 1 for c in r.json())


def test_comment_email_format():
    body = requests.get(f"{BASE_URL}/comments/1", timeout=TIMEOUT).json()
    assert "@" in body["email"]


def test_comment_body_not_empty():
    body = requests.get(f"{BASE_URL}/comments/1", timeout=TIMEOUT).json()
    assert body["body"].strip() != ""
