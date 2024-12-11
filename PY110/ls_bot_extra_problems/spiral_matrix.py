# Problem
# - Input
#     - Integer n
# - Output
#     - returns n x n nested matrix  of elements from 1 to n^2 in a spiral order
# - Explicit Rules
#     - spiral order starts from top left and moves clockwise
# - Implicit Rules
# - Question

#Examples

    # # Test case 1: 1x1 matrix
    # assert create_spiral_matrix(1) == [[1]]

    # # Test case 2: 2x2 matrix
    # assert create_spiral_matrix(2) == [[1, 2], [4, 3]]

    # # Test case 3: 3x3 matrix
    # assert create_spiral_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    # # Test case 4: 4x4 matrix
    # assert create_spiral_matrix(4) == [
    #     [1, 2, 3, 4],
    #     [12, 13, 14, 5],
    #     [11, 16, 15, 6],
    #     [10, 9, 8, 7]
    # ]

    # # Test case 5: 5x5 matrix
    # assert create_spiral_matrix(5) == [
    #     [1, 2, 3, 4, 5],
    #     [16, 17, 18, 19, 6],
    #     [15, 24, 25, 20, 7],
    #     [14, 23, 22, 21, 8],
    #     [13, 12, 11, 10, 9]
    # ]

    # # Test case 6: 0x0 matrix (edge case)
    # assert create_spiral_matrix(0) == []

#Data Structures
# - nested list for the spiral matrix

#Algorithm
# 1. get all of the numbers from 1 to n^2
# 2. create a n x n matrix
# 3. create first_row variable = 0
# 4. create last_row variable = n
# 5. create first_column variable = 0
# 6. create last_column variable = n


#Code
def create_spiral_matrix(n):
    number_list = list(range(1, n**2 + 1))
    nxn_matrix = []
    for _ in range(n):
        new_inner_list = []
        for index in range(n):
            new_inner_list.append(None)
        nxn_matrix.append(new_inner_list)
    # print(nxn_matrix)
    first_row = 0
    last_row = n
    first_column = 0
    last_column = n
    while len(number_list) > 0:
    #     new_inner_list = []
        for index in range(n):
            if(nxn_matrix[first_row][index] == None):
                nxn_matrix[first_row][index] = number_list.pop(0)
        first_row += 1
        for index in range(n):
            if(nxn_matrix[index][last_column -1] == None):
                nxn_matrix[index][last_column -1] = number_list.pop(0)
        last_column -= 1
        for index in range(n):
            if(nxn_matrix[last_row-1][last_column -1-index] == None):
                nxn_matrix[last_row-1][last_column -1-index] = number_list.pop(0)
        last_row -= 1
        for index in range(n):
            if(nxn_matrix[last_row-1-index][first_column] == None):
                nxn_matrix[last_row-1-index][first_column] = number_list.pop(0)
        first_column += 1
        # break
    #     first_row += 1
    #     break
    #     for _ in range(n - last_column):
    print(nxn_matrix)
    return nxn_matrix
# # Test case 1: 1x1 matrix
# assert create_spiral_matrix(1) == [[1]]

# Test case 2: 2x2 matrix
print(create_spiral_matrix(2) == [
    [1, 2], 
    [4, 3]
])

# Test case 3: 3x3 matrix
print( create_spiral_matrix(3) == [
    [1, 2, 3], 
    [8, 9, 4], 
    [7, 6, 5]
])

# Test case 4: 4x4 matrix
print(create_spiral_matrix(4) == [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
])

# Test case 5: 5x5 matrix
print(create_spiral_matrix(5) == [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
])

# # Test case 6: 0x0 matrix (edge case)
print(create_spiral_matrix(0) == [])