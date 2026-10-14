def count_element(items, element):
    count = 0
    for item in items:
        if item == element:
            count += 1
    return count


print("Number of 2s:", count_element([1, 2, 2, 3], 2))
