score = 100
if(score>90):
    print("You passed the exam with flying colors!")
elif(score>33):
    print("You passed the exam")
else:
    print("You need to retake the exam")

status_code = 400
if status_code == 200:
    print("TestCase passed")
elif status_code == 404:
    print("Not found")
else:
    print("Test Failed unexpected status code", status_code)

username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Login Failed")