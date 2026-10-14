import re

text = "Python123 is easy456"

result = re.findall(r'\d', text)

print(result)
