fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(3):
    print(fruits[i])

print(list(range(3)))
print(list(range(1,9)))
print(list(range(0,10,2)))

status_codes = [200,404,200,500,201]

for code in status_codes:
    if code == 200 or code == 201:
        print(code, '-> PASS')
    else:
        print(code, '-> FAIL')

all_codes = [200,201,404,400,403,500]
failed_codes = []

for code in all_codes:
    if code == 200 or code == 201:
        print("OK")
    else:
        failed_codes.append(code)

print(failed_codes)
print(len(failed_codes))

api_responses = [
    {'url': '/api/users', 'status':200},
    {'url': '/api/orders', 'status': 300},
    {'url': '/api/login', 'status': 500},
]

print("------- API TEST RESULTS ------")

for response in api_responses:
    if response['status'] == 200:
        print("Pass -> ", response['url'])
    else:
        print("Fail -> ", response['url'])
