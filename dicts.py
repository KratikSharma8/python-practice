user = {
    'name':'kratik',
    "age":20,
    "Gender":"Male"
}

print(user)
print(user['name'])
print(user['age'])
print(user['Gender'])
print(len(user))

print("name" in user)
print("country" in user)

user['country'] = "India"
user['age'] = 21
print(user)
print(user['age'])

for key in user:
    print(key, ":", user[key])

api_response = {
    'status': 200,
    "data": {
        "id": 1,
        "name": "kratik",
        "age": 20
    }
}

print(api_response['status'])
print(api_response['data']['id'])
print(api_response['data']['name'])
print(api_response['data']['age']) 

responses = [
    {'url': '/api/users/1', 'status': 200, 'has_data': True},
    {'url': '/api/users/999', 'status': 404, 'has_data': False},
    {'url': '/api/orders', 'status': 500, 'has_data': False},
]

for r in responses:
    if r['status'] == 200 and r['has_data']:
        print("Pass: ", r['url'])
    else:
        print("Fail: ", r['url'], "with status", r['status'])