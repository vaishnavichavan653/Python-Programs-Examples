with open("sample_text.txt", "w") as file:
    file.write("First line\nSecond line\nThird line\n")

with open("sample_text.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())
