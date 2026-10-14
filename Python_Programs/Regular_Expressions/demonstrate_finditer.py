import re

text = "Python 10 Java 20 C 30"

for match in re.finditer(r'\d+', text):
    print(match.group(), match.start())
