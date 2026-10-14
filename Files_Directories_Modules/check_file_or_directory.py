import os

name = input("Enter a file or folder name: ")

if os.path.isfile(name):
    print("It is a file.")
elif os.path.isdir(name):
    print("It is a directory.")
else:
    print("It does not exist.")
