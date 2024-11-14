def unique_sequence(list1):
    number = 0
    new_list = []
    for each in list1:
        if each != number:
            new_list.append(each)
            number = each
    return new_list

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True