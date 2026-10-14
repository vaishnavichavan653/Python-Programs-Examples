try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

finally:
    print("Execution completed")
