import re

pin = input("Enter PIN code: ")

if re.fullmatch(r'[1-9][0-9]{5}', pin):
    print("Valid PIN code")
else:
    print("Invalid PIN code")
