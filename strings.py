word = "automation"

print("Length of the word:", len(word))
print("First character:", word[0])
print("Last character:", word[-1])
print("Upper Case:", word.upper())
print("Lower Case:", word.lower())
print("Replace auto with manual:", word.replace("auto", "manual"))

email = " kratik@gmail.com "
print("Length of the email:", len(email))
email = email.strip()  # Remove leading and trailing whitespace
print("Length of the email:", len(email))
print("Email after stripping:", email)
print("Email contains @:", "@" in email)
print("Email starts with 'kratik':", email.startswith("kratik"))

#print(email[50])
print(email[0:5])

api_response = "  Success: User created successfully  "
is_clean = api_response.strip().lower()
print(is_clean)
print(is_clean=="success: user created successfully")
