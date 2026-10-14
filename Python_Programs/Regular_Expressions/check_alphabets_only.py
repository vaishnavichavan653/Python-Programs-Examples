import re

text = input("Enter a string: ")

if re.fullmatch(r'[a-zA-Z]+', text):
    print("Contains only alphabets")
else:
    print("Contains other characters")
