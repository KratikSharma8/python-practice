# Odd or even?

def odd_or_even(number):
    if(number % 2 == 0):
        return "Even"
    else:
        return "Odd"
    
print(odd_or_even(40))
print(odd_or_even(41))

#Dictionary Practice

dict = {
        "name": "Kratik",
        "email": "kratik@example.com",
        "role": "QA Engineer"
    }

#Loops Practice

status_codes = [200, 404, 201, 500, 403]
for code in status_codes:
    print(code)
    if code == 200:
        print("Pass")
    else:
        print("Fail")


