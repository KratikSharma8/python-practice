def test_get_failed_codes():
    result = get_failed_codes([200,404,201,500])
    assert 404 in result
    assert 500 in result
    assert 200 not in result
    assert 201 not in result

def test_validate_user():
    user = {'name':"Kratik",'email':"kratik@example.com"}
    user1 = {'name':"Kratik"}
    assert validate_user(user) == "Pass"
    assert validate_user(user1) == "Fail - Missing Email"

def validate_user(user):
    if 'name' not in user:
        return "Fail - Missing Name"
    elif 'email' not in user:
        return "Fail - Missing Email"
    else:
        return "Pass"
    
def get_failed_codes(codes):
    failed_codes = []
    for code in codes:
        if code != 200 and code != 201:
            failed_codes.append(code)
    return failed_codes
