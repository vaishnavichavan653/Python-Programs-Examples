text = "Hello Python"
letter_counts = {}

for letter in text.lower():
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)
