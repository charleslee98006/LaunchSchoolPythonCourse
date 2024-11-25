#Problem
# Input:
#     - list of numbers, all but 1 are duplicates
# Output:
#     - return the different number
# Explicit Rules:
#     - input list will always have 3 numbers minimum
#     - will have 1 exact number that is different
# Implicit Rules:
#     - floats are included
# Question:
#     - 
# #Examples
# # print(what_is_different([0, 1, 0]) == 1)
# # print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# # print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# # print(what_is_different([3, 4, 4, 4]) == 3)
# # print(what_is_different([4, 4, 4, 3]) == 3)

# #Data Structures
# -set to get the unique values
# - list to get the number based on the count

# #Algo
# def what_is_different(list1):
#     1.get the unique values from list into sets
#     2. get the value where the count is equal to 1
#     3. return the value
    
#Code
def what_is_different(list1):
    new_set = set(list1)
    filtered_list = [number for number in list1 if list1.count(number) == 1]
    return filtered_list[0]


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
