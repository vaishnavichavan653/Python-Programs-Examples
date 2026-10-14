from array import array

numbers = array("i", [10, 20, 30])
print("Original array:", numbers.tolist())

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(20)

print("Updated array:", numbers.tolist())
print("First item:", numbers[0])
print("Number of items:", len(numbers))
