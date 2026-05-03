import requests

def test_base_url(api_base_url):
    assert api_base_url == "http://127.0.0.1:8000"

def test_new_user(new_user):
    assert new_user['name'] == "Rakesh Sharma"

def test_user_created(user_created):
    assert user_created.status_code == 201
