#Problem
# -Input
#     -int list
#     - function is_groupA
#         - takes in an in and returns boolean
# -Output
#     - tuple containing two list
#         -first list: all elements where is_groupA = True
#         -second list: all elements where is_group = False
# -Explicit Rules
#     - relative orders in original list needs to be preserved
# -Implicit Rules
#     -

#Examples

# # Test cases
# def is_even(n):
#     return n % 2 == 0

# def is_positive(n):
#     return n > 0

# print(partition_list([1, 2, 3, 4, 5, 6], is_even) == ([2, 4, 6], [1, 3, 5]))
# print(partition_list([-2, -1, 0, 1, 2], is_positive) == ([1, 2], [-2, -1, 0]))
# print(partition_list([], is_even) == ([], []))
# print(partition_list([1, 3, 5], is_even) == ([], [1, 3, 5]))
# print(partition_list([2, 4, 6], is_even) == ([2, 4, 6], []))

#Data Structure


#Algo
# def partition_list(list1, function):
#     true_list = [ number in list1 if function(number)]
#     false_list = [ number in list1 if not function(number)]


#Code
def partition_list(list1, function):
    true_list = [number for number in list1 if function(number)]
    false_list = [number for number in list1 if not function(number)]
    return (true_list, false_list)

# Test cases
def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

print(partition_list([1, 2, 3, 4, 5, 6], is_even) == ([2, 4, 6], [1, 3, 5]))
# print(partition_list([-2, -1, 0, 1, 2], is_positive) == ([1, 2], [-2, -1, 0]))
# print(partition_list([], is_even) == ([], []))
# print(partition_list([1, 3, 5], is_even) == ([], [1, 3, 5]))
# print(partition_list([2, 4, 6], is_even) == ([2, 4, 6], []))