import re

text = "I have 12 pens and 25 books"

result = re.findall(r'\d+', text)

print(result)
