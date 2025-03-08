email = input("Please enter your Email: ")

valid_domains = ["gmail.com", "yahoo.com", "outlook.com"]
if "@" not in email:
    print("Error: Email must contain '@'.")

elif " " in email:
    print("Error: Email must not contain spaces.")

else:
    before_at, after_at = email.split("@", 1)

    if len(before_at) < 5:
        print("Error: The part before '@' must be at least 5 characters long.")
    elif after_at not in valid_domains:
        print("Error: Invalid email domain. Allowed: gmail.com, yahoo.com, outlook.com.")
    else:
        print("Valid Email ")
