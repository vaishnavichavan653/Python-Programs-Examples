with open("sample_text.txt", "w") as file:
    file.write("Python is easy")

with open("sample_text.txt", "r") as file:
    text = file.read().lower()

vowels = 0
consonants = 0

for letter in text:
    if letter.isalpha():
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
