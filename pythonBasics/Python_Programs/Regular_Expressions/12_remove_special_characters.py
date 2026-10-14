import re

text = "Hello@123#Python!"

result = re.sub(r'[^a-zA-Z0-9 ]', '', text)

print(result)
