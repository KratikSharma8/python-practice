import requests

Base_url = "http://127.0.0.1:8000"

def test_get_user_returns_200():
    response = requests.get(f'{Base_url}/api/users/1')
    assert response.status_code == 200

def test_get_user_has_data_key():
    response = requests.get(f'{Base_url}/api/users/1')
    data = response.json()
    assert 'data' in data

def test_user_has_email():
    response = requests.get(f'{Base_url}/api/users/1')
    data = response.json()
    assert 'email' in data['data']

def test_user_email_has_at_symbol():
    response = requests.get(f'{Base_url}/api/users/1')
    data = response.json()
    assert '@' in data['data']['email']

def test_user_name_is_correct():
    response = requests.get(f'{Base_url}/api/users/1')
    data = response.json()
    assert data['data']['name'] == 'Kratik Sharma'

def test_user_not_found_returns_404():
    response = requests.get(f'{Base_url}/api/users/999')
    assert response.status_code == 404

def test_missing_user_has_error_message():
    response = requests.get(f'{Base_url}/api/users/999')
    data = response.json()
    assert 'detail' in data

def test_get_all_users_returns_200():
    response = requests.get(f'{Base_url}/api/users')
    assert response.status_code == 200

def test_user_list_has_total_key():
    response = requests.get(f'{Base_url}/api/users')
    data = response.json()
    assert 'total' in data

def test_user_list_is_not_empty():
    response = requests.get(f'{Base_url}/api/users')
    data = response.json()
    assert len(data['data']) > 0

def test_user_list_total_is_correct():
    response = requests.get(f'{Base_url}/api/users')
    data = response.json()
    assert data['total'] == 3

def test_each_user_has_required_fields():
    response = requests.get(f'{Base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert 'id' in user
        assert 'name' in user
        assert 'email' in user
        assert 'role' in user

def test_each_user_email_is_valid():
    response = requests.get(f'{Base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert '@' in user['email']

def test_each_user_has_a_role():
    response = requests.get(f'{Base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert user['role'] in ['admin', 'user']

def test_invalud_user_returns_404():
    response = requests.get(f'{Base_url}/api/users/999')
    assert response.status_code == 404

def test_invalid_user_returns_error_detail():
    response = requests.get(f'{Base_url}/api/users/999')
    data = response.json()
    assert 'detail' in data
    assert data['detail'] == 'User not found'

def test_user_zero_returns_404():
    response = requests.get(f'{Base_url}/api/users/0')
    assert response.status_code == 404

def test_negative_user_id_returns_404():
    response = requests.get(f'{Base_url}/api/users/-1')
    assert response.status_code == 404

