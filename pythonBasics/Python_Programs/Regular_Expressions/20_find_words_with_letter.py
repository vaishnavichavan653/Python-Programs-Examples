import re

text = "apple mango orange banana"

result = re.findall(r'\b\w*a\w*\b', text)

print(result)
