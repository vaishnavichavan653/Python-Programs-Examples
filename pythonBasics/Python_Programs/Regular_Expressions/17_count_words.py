import re

text = "Python is easy to learn"

result = re.findall(r'\b\w+\b', text)

print("Number of words:", len(result))
