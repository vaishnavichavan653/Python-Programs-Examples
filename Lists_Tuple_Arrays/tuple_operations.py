fruits = ("apple", "banana", "orange", "banana")

print("Tuple:", fruits)
print("First item:", fruits[0])
print("Items from index 1 to 2:", fruits[1:3])
print("Number of bananas:", fruits.count("banana"))
print("Index of orange:", fruits.index("orange"))

for fruit in fruits:
    print(fruit)
