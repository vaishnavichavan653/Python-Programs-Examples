try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a + b

except ValueError:
    print("Invalid input")

else:
    print("Sum:", result)
