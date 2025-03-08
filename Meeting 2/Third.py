password = input("Please enter your password: ")

if len(password) < 8:
    print("Error: Password is too short. It must be at least 8 characters long.")

elif not any(char.isdigit() for char in password):
    print("Error: Password must contain at least one number.")

elif password.lower() == password or password.upper() == password:
    print("Error: Password must contain at least one uppercase and one lowercase letter.")

elif not any(char in "!@#$%&" for char in password):
    print("Error: Password must contain at least one special character (!@#$%&).")

else:
    print("Strong Password!")
