text = "Hello Python"
vowels = 0

for letter in text.lower():
    if letter in "aeiou":
        vowels += 1

print("Number of vowels:", vowels)
