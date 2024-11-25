#Problem
# Input:
#     - list of integers
# Output:
#     - integer of index N or -1 if no index
# Explicit Rules:
#     -Return N which all numbers with an index less than N sum to the same value as the numbers with an index greater than N
#     - if have more than 1 index as answer, give the smallest one
# Implicit Rules:
#     -
# Question:
#     - 
# #Examples

# # print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# # print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# # print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# # print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # # The following test case could return 0 or 3. Since we're
# # # supposed to return the smallest correct index, the correct
# # # return value is 0.
# # print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

# #Data Structures
# - List of all combinations sums equal to each 

# #Algo
# def equal_sum_index(list1):
#     1. place a pointer at the first index position and do the following:
#         1. check to see the the left side of the index values equal to the right side
#         2. if yes, add the index position to a list
#     2. return the small index position from list

    
#Code
def equal_sum_index(list1):
    new_list = [index for index in range(len(list1)) if sum(list1[:index]) == sum(list1[index+1:])]
    if (new_list):
        return min(new_list)
    else:
        return -1


print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3) # [7, 4, 7]
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1) # [7, 51, 7]
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)