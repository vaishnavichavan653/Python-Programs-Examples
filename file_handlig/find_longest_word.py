with open("sample_text.txt", "w") as file:
    file.write("Python makes reading files easy")

with open("sample_text.txt", "r") as file:
    words = file.read().split()

longest_word = max(words, key=len)
print("Longest word:", longest_word)
