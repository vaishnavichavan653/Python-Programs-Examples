with open("story.txt", "w") as file:
    file.write("Python is easy to learn.")

with open("story.txt", "r") as file:
    text = file.read()

print("Characters:", len(text))
print("Words:", len(text.split()))
