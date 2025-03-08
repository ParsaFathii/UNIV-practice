national_number = input("Please enter your national number: ")
age = int(national_number[:2])
if 0 <= age <= 10:
    print("You are below 25 years old.")
elif 60 <= age <= 90:
    print("You are above 30 years old.")
else:
    print("You are between 25 to 30 years old.")