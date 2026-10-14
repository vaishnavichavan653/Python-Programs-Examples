import re

text = input("Enter a string: ")

if re.fullmatch(r'[a-zA-Z0-9]+', text):
    print("Alphanumeric string")
else:
    print("Contains special characters")
