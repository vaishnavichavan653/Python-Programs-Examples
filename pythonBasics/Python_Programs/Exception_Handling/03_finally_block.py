try:
    a = int(input("Enter a number: "))
    print("Number:", a)

except ValueError:
    print("Invalid input")

finally:
    print("Finally block executed")
