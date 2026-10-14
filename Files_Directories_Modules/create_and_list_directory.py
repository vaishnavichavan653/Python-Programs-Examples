import os

folder_name = "MyFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created.")
else:
    print("Folder already exists.")

print("Items in the current directory:")
for item in os.listdir("."):
    print(item)
