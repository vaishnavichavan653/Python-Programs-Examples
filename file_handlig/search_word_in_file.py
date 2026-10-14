search_word = input("Enter a word to search for: ").lower()

with open("sample_text.txt", "w") as file:
    file.write("Python is easy.\n")
    file.write("Python reads and writes files.\n")
    file.write("Files are useful.\n")

matches = 0
with open("sample_text.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        count = line.lower().split().count(search_word)
        if count > 0:
            matches += count
            print("Found on line:", line_number)

print("Number of occurrences:", matches)
