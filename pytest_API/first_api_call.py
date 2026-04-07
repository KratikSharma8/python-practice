import requests
from config import API_KEY

headers = {
    "x-api-key": API_KEY
}

response = requests.get("https://reqres.in/api/users/1", headers=headers)

print("Status Code:", response.status_code)
print()

data = response.json()
print(data)
print()
print("Just the User Data:")
print(data['data'])

print()
print("User Fields:")
print("ID:", data['data']['id'])
print("Email:", data['data']['email'])
print("First Name:", data['data']['first_name'])
print("Last Name:", data['data']['last_name'])

for key_value in data['data'].items():
    print(key_value[0], ":", key_value[1])

response = requests.get("https://reqres.in/api/users/", headers = headers)
print("Status Code:", response.status_code)
data2 = response.json()
print("Response Body:", data2)
print("Headers:", response.headers['content-type'])

print("-----------User Report---------")
for user in data2['data']:
    name = user['first_name'] + " " + user['last_name']
    email = user['email']
    
    if '@reqres.in' in email:
        domain = "Internal User"   
    else:
        domain = "External User"

    print(f"{name} - {email} {domain}")