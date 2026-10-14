import shutil

with open("original.txt", "w") as file:
    file.write("This is the original file.")

shutil.copy("original.txt", "copy.txt")
print("Copied original.txt to copy.txt")
