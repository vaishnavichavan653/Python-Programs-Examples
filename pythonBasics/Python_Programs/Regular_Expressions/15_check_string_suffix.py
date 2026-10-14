import re

text = "I am learning Python"

if re.search(r'Python$', text):
    print("String ends with Python")
else:
    print("String does not end with Python")
