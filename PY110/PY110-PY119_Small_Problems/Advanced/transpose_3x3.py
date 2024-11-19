def transpose(list1):
    new_list = []
    for index in range(len(list1)):
        new_inner_list = []
        for index2 in range(len(list1[index])):
            new_inner_list.append(list1[index2][index])
        new_list.append(new_inner_list)
    return new_list

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True