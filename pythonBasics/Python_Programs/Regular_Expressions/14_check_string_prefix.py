import re

text = "Python is easy"

if re.match(r'^Python', text):
    print("String starts with Python")
else:
    print("String does not start with Python")
