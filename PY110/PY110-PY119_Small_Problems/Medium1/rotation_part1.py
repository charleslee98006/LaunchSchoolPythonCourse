#P
# Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.

# Input:
#     -
# Output:
#     -
# Explicit Rules:
#     -
# Implicit Rules:
#     -
# Question:
    # - 
#E


#D


#A
def rotate_list(list1):
    if type(list1) != list:
        return None
    elif len(list1):
        new_list = list1[1:len(list1)]
        new_list.append(list1[0])
        return new_list
    return []
#C

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])