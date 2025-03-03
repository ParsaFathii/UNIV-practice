username = input("Please enter your username : ")
password = input("Please enter your password : ")

if len(username or password) < 4:
    print("Error : your username or password Isempty")
    exit()

if len(password) < 8:
    print("Error : your password must be upper than 8")
    exit()

has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if not has_digit or not has_upper:
    print("Error: Password must one number and one uppercase letter.")
    exit()

if username == "admin":
    print("ورود مدیر")
else:
    print("ورود موفق")
