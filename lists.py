fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(len(fruits))

# apple
# banana
# cherry
# cherry
# 3

fruits.append("pineapple")
fruits.append("grape")
print(fruits)
fruits.insert(0, "orange")
print(fruits)
fruits.append("banana")
print(fruits)
fruits.remove("banana")
print(fruits)
print(len(fruits))
fruits.pop()
print(fruits)
print(len(fruits))

# ['apple', 'banana', 'cherry', 'pineapple', 'grape']
# ['orange', 'apple', 'banana', 'cherry', 'pineapple', 'grape']
# ['orange', 'apple', 'banana', 'cherry', 'pineapple', 'grape', 'banana']
# ['orange', 'apple', 'cherry', 'pineapple', 'grape', 'banana']
# 6
# ['orange', 'apple', 'cherry', 'pineapple', 'grape']
# 5

print("apple" in fruits)
print("Mango" in fruits)

allowed_fruits = ["apple", "banana", "cherry"]
user_input = input("Enter a fruit: ")

if user_input in allowed_fruits:
    print("Your fruit is allowed.")
else:
    print("Your fruit is not allowed.")


response_time = [200,300,12.3,210,510]
average_time = sum(response_time) / len(response_time)
print("Average response time:", average_time)
sorted_times = sorted(response_time)
print(sorted_times)

print("Fastest response time is : ", max(response_time))
print("Slowest response time is : ", min(response_time))
print("Length response time is : ", len(response_time))


error_messages = ['timeout', 'connection refused', 'invalid token']
#assert "error" in error_messages
assert "timeout" in error_messages

required_fields = ['name', 'email', 'phone']
assert 'name' in required_fields
assert "email" in required_fields
#assert "Kishan" in required_fields
