age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Not eligible to vote")
    print("Eligible to vote")

except ValueError as e:
    print(e)
