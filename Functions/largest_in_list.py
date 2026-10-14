def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print("Largest number:", largest_number([4, 9, 2, 7]))
