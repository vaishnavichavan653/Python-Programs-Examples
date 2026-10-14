with open("sample_text.txt", "w") as file:
    file.write("Python is fun.")

with open("sample_text.txt", "r") as file:
    text = file.read()

print("Characters including spaces:", len(text))
