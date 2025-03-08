card_number = input("Please enter your card number: ")
if len(card_number) != 16:
    print("Invalid ID card number")
elif not card_number.isdigit():
    print("Invalid ID card number")
elif card_number.startswith("6274"):
    print("Bank: Saman")
elif card_number.startswith("6037"):
    print("Bank: Mellat")
elif card_number.startswith("5893"):
    print("Bank: Saderat")
else:
    print("Unknown bank")
