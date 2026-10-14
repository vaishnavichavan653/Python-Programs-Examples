def is_prime(number):
    if number < 2:
        return False

    for value in range(2, number):
        if number % value == 0:
            return False

    return True


print("Is 7 prime?", is_prime(7))
