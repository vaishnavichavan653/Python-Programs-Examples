with open("sample_text.txt", "w") as file:
    file.write("python is easy and python is useful")

with open("sample_text.txt", "r") as file:
    words = file.read().lower().split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
