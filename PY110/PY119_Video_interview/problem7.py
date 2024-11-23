#Problem
# -Input
#     - list of integers
# -Output
#     - return the number of identical pairs of integer
# -Explicit Rules
#     - empty list return 0
#     - overlapping pairs do not count, complete pairs only
# -Implicit Rules
#     - Order does not matter
#     - single element list is zero
# -Question

#Examples
# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

#Data structures
# -list

#Algo
# def pairs(list1):
#     1.sort list1 in ascending order
#     2. get a tally of non-overlapping duplicates from the list
#     3. add all of the tally and return the sum

#Code
def pairs(list1):
    list.sort(list1)
    # print(list1)
    new_set = set(list1)
    new_list = [list1.count(number)//2 for number in new_set]
    return(sum(new_list))

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)