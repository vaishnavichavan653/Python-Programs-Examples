values = ["Python", [10, 20, 30], {"name": "Ava", "age": 20}]

for value in values:
    print(f"{type(value).__name__} length:", len(value))

print("Integer addition:", 5 + 3)
print("String concatenation:", "Hello, " + "Python")
print("List concatenation:", [1, 2] + [3, 4])
