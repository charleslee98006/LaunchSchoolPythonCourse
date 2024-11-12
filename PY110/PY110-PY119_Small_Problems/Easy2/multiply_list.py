#P
#
# Write a function that takes two list arguments, each containing a list of numbers, and returns a new list 
# that contains the product of each pair of numbers from the arguments that have the same index. 
# You may assume that the arguments contain the same number of elements.
# Input:
#     - two list
# Output:
#     - new list of the products from the same index
# Explicit Rules:
#     - each input list contains numbers
#     - each input list have the same number of elements
#     - products are numbes from the same indices
# Implicit Rules:
#     -
# Question:
#     - 
#E
# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

#D
# -

#A
# def multiply_list(parameter):
#     1.
#C
import math
def multiply_list(list1, list2):
    return [list1[index]* list2[index] for index in range(0, len(list1))]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True