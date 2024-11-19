

def rotate90(list1):
    # new_list = []
    # for index in range(len(list1[0])):
    #     # print('index: ', index)
    #     new_inner_list = []
    #     for index2 in range(len(list1)):
    #         # print(list1[index2][index])
    #         new_inner_list.append(list1[index2][index])
    #     new_list.append(list(reversed(new_inner_list)))
    # print(new_list)
    return [list(reversed([list1[index2][index] for index2 in range(len(list1))])) for index in range(len(list1[0]))] 


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)