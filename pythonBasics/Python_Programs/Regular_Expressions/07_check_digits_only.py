import re

text = input("Enter a string: ")

if re.fullmatch(r'[0-9]+', text):
    print("Contains only digits")
else:
    print("Contains other characters")
