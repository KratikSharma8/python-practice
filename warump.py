def get_failed_codes(codes):
    failed_codes = []
    for code in codes:
        if code != 200 and code != 201:
            failed_codes.append(code)

    return failed_codes

x = get_failed_codes([200, 404, 201, 500, 403])
print(x)


def validate_user(user):
    if 'name' not in user:
        return "Fail - Missing Name"
    elif 'email' not in user:
        return "Fail - Missing Email"
    else:
        return "Pass"
    
print(validate_user({'name': 'Kratik', 'email': 'k@test.com'}))
print(validate_user({'name': 'Kratik'}))