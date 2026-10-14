try:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        raise ValueError("Number must be positive")

    print("Number:", num)

except ValueError as e:
    print("Error:", e)
