def unique_items(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


print("Unique items:", unique_items([1, 2, 2, 3, 1]))
