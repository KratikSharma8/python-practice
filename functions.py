def greet(name):
    return "Hello, " + name + "!"

print(greet("kishan"))

def add(a,b):
    return a+b

print(add(4,3))
print(add(10,5))
print(add("Kratik"," Sharma"))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

def validate_user(user):
    if "name" not in user:
        return "Name Missing"
    if "age" not in user:
        return "Age Missing"
    if "@" not in user['email']:
        return "Invalid Email"
    return "User Validated"

user1 = {'name': "Kratik", "age": 25, "email": "kratik@example.com"}
user2 = {'name': "Kishan", "age": 30, "email": "kishanexample.com"}
user3 = {'age': 22, "email": "user3@example.com"}
# user4 = {'name': "User4", "age": 25}

print(validate_user(user1))
print(validate_user(user2))
print(validate_user(user3))
# print(validate_user(user4))

def no_return(name):
    greeting = 'Hello ' + name

result = no_return('Kratik')
print(result)