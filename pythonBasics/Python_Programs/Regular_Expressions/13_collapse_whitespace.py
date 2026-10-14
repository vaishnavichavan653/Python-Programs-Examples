import re

text = "Python    is   very    easy"

result = re.sub(r'\s+', ' ', text)

print(result)
