import requests

Base_url = "http://127.0.0.1:8000/"

data = requests.get(f"{Base_url}/api/users/1")
print("Status Code:", data.status_code)
print("Response Body:", data.json())

data = data.json()

print("Top Level Keys:", list(data.keys()))
print("User Keys:", list(data['data'].keys()))


print("ID:", data['data']['id'])
print("Name:", data['data']['name'])
print("Email:", data['data']['email'])
print("Role:", data['data']['role'])

list_response = requests.get(f'{Base_url}/api/users')
list_data = list_response.json()

print("Total Users:", list_data['total'])
print("Users on this Page:", len(list_data['data']))

print("-----------User Report -----------")
for user in list_data['data']:
    print(f"{user['name']} | {user['email']} | {user['role']}")

print("----------- Role Check -----------")
for user in list_data['data']:
    if user['role'] == 'admin':
        print(f"{user['name']} is an admin")
    else:
        print(f"{user['name']} is an user")

print("----------- Missing User ------------")
missing = requests.get(f'{Base_url}/api/users/999')
print("Missing user status: ", missing.status_code)
print("Missing User Body:", missing.json())

