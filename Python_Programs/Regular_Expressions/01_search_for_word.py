import re

text = "Python is a programming language"

result = re.search("Python", text)

if result:
    print("Word found")
else:
    print("Word not found")
