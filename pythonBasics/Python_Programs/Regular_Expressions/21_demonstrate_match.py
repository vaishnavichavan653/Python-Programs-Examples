import re

text = "Python programming"

result = re.match(r'Python', text)

if result:
    print("Match found")
else:
    print("No match")
