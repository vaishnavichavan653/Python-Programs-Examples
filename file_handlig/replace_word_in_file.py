old_word = input("Word to replace: ")
new_word = input("New word: ")

with open("sample_text.txt", "w") as file:
    file.write("Python is fun. I like Python.")

with open("sample_text.txt", "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open("updated_text.txt", "w") as file:
    file.write(text)

print("Updated text saved to updated_text.txt")
