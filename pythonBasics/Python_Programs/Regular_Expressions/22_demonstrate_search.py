import re

text = "I am learning Python"

result = re.search(r'Python', text)

if result:
    print("Match found at position:", result.start())
else:
    print("No match")
