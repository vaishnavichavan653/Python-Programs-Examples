import re

text = "Python Is An Easy Language"

result = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)

print(result)
