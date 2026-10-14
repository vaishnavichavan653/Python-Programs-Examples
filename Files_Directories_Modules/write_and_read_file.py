with open("message.txt", "w") as file:
    file.write("Hello! This text is saved in a file.\n")

with open("message.txt", "r") as file:
    print(file.read())
