def multiply_items(list1, list2):
    return [list1[index] * list2[index] for index in range(0, len(list1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True