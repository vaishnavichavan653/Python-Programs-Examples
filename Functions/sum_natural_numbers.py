def sum_natural_numbers(number):
    total = 0
    for value in range(1, number + 1):
        total += value
    return total


print("Sum:", sum_natural_numbers(5))
