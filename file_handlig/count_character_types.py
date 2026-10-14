with open("sample_text.txt", "w") as file:
    file.write("Python 3 is fun!")

with open("sample_text.txt", "r") as file:
    text = file.read()

letters = digits = spaces = special = 0

for character in text:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1
    elif character == " ":
        spaces += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
