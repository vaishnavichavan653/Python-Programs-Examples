def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


print("Power:", power(2, 3))
