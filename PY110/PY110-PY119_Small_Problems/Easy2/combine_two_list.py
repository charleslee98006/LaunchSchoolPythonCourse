#P
# Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.
# You may assume that both input lists are non-empty, and that they have the same number of elements.

# Input:
#     - two lists
# Output:
#     - new list containing all elements from both list
# Explicit Rules:
#     - lists are non-empty
#     - have the same number of elements
#     - elements have to alternate
# Implicit Rules:
#     -
# Question:
#     - 
#E
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True

#D
# - list

#A
# def interleave(parameter):
#     1.
#C


def interleave(list1, list2):
    new_list = []
    for index in range(0, len(list1)):
        new_list.append(list1[index])
        new_list.append(list2[index])
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True