#P
# Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. 
# Put the first half of the original list elements in the first element of the return value and put the second half in the second element. 
# If the original list contains an odd number of elements, place the middle element in the first half list.
# Input:
#     - takes a list
# Output:
#     -returns a list containing two elements; each element are a list
# Explicit Rules:
#     - first half into first element list
#     - second half into second element list
#     - if original list has odd number of elements -> goes with the first half list
# Implicit Rules:
#     - will need to have two lists
#     - in case of 1 element, you will need to have a second half list empty
# Question:
#     - 
# #E
# -
# # All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

#D
# - 2 lists and wrapping it with an outer list

#A
# def halvsies(original_list):
#     1.create two empty lists; first one would be call `first half` second will be call `second half`
#     2. find out if the len of original list is odd or even
#      1. if odd - slice list to the middle with the odd element and assign to first half, the rest to second half
#      2. if even - slice list from middle and assign the first half and second half accordingly.
#     3. wrap a list around the first half list and the second half list and return it

#C
def halvsies(original_list):
    middle_index = len(original_list)//2
    if(len(original_list) % 2 == 1):
        middle_index = middle_index+1
    return [ original_list[:middle_index], original_list[middle_index:]]

    
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])