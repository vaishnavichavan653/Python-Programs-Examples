try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Result:", a / b)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Division by zero is not allowed")

except Exception as e:
    print("Error:", e)
