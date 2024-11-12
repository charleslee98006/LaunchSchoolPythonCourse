#P
# Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. 
# You may assume that both arguments will always be lists.
# 
# Input:
#     - takes 2 list
# Output:
#     - returns a set contains unions of values from two list
# Explicit Rules:
#     - Always be a list
#     - 
# Implicit Rules:
#     - sets will take out duplicates
# Question:
#     - 
#E
# -
# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

#D
# - a new list and a new set

#A
# def union(list1, list2):
#     1. combine list1 and list 2 into one list
#     2. convert combined list into set
#     3. return set

#C
def union(list1, list2):
    return set(list1 + list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True