def even_numbers(number):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

numbers = [1,2,3,4,5,6,7,8,9,10]
print(even_numbers(numbers))

def validate_users(user):
    if "name" not in user:
        return "FAIL - No user"
    if "email" not in user:
        return "FAIL - No email"
    if "@" not in user['email']:
        return "FAIL - Invalid Email"
    if "role" not in user:
        return "FAIL - No Role"
    if len(user['name']) < 3:
        return "FAIL - Name too short"
    return "User Validated"

def run_tests(users):
    passed = 0
    failed = 0
    for user in users:
        result = validate_users(user)
        name = user.get("name", "Unknow")
        print(name, ":", result)

        if result == "User Validated":
            passed += 1
        else:
            failed += 1

    print("------------")
    print("Total", passed+failed)
    print("Passed", passed)
    print("Failed", failed)

test_users = [
    {'name': 'Kratik', 'email': 'k@test.com', 'role': 'admin'},
    {'name': 'Rahul', 'email': 'rahul@test.com'},
    {'name': 'Priya', 'email': 'not-an-email', 'role': 'user'},
    {'email': 'someone@test.com', 'role': 'user'},
    {'name': 'Amit', 'email': 'amit@test.com', 'role': 'user'},
    {'name': 'A', 'email': 'a@test.com', 'role': 'user'},
]

run_tests(test_users)