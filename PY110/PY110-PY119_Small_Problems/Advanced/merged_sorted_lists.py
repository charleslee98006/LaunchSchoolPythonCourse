#Problem
# -Input
#     - Two lists
# -Output
#     -1 combined list sorted
# -Explicit Rules
#     - list with only contain all int or all strings
#     - resulting list must be ascending order
#     - You may not provide any solution that requires you to sort the result list
# -Implicit Rules
# -Question

#Example

# # All of these examples should print True
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

#Data structure
# - Lists

#Algo
# def merge(list1, list2):
#     1. combine the two list into one and assign unsorted_list to the combination
#     2. Create a variable called result_list assign with a empty list
#     3. in a loop of the combined list do the following:
#         1. go through two elements and get the lowest element
#         2. place the lowest element onto the result_list
#     4. return result_list
#Code
def merge(list1, list2):
    unsorted_list = list1 + list2
    result_list = []
    while len(unsorted_list) > 0 :
        result_list.append(unsorted_list.pop(unsorted_list.index(min(unsorted_list))))
    return result_list
    
# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)