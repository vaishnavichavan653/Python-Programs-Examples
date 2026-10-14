with open("sample_text.txt", "w") as file:
    file.write("Python is easy.\n")
    file.write("Files can store text.\n")
    file.write("This is a sample file.\n")

with open("sample_text.txt", "r") as file:
    print("Number of lines:", len(file.readlines()))
