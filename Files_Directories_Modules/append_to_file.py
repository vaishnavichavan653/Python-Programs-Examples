with open("notes.txt", "a") as file:
    file.write("This is a new note.\n")

with open("notes.txt", "r") as file:
    print(file.read())
