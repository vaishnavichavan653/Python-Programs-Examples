with open("sample_text.txt", "w") as file:
    file.write("Python makes file handling easy.")

with open("sample_text.txt", "r") as file:
    words = file.read().split()

print("Number of words:", len(words))
