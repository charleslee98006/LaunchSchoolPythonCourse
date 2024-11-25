# #Problem
# Input:
#     - list of integers
# Output:
#     - returns int with odd number of frequency
# Explicit Rules:
#     -  will always have 1 value that has odd number of frequency in the argument
# Implicit Rules:
#     -
# Question:
#     - 
# #Examples

# # print(odd_fellow([4]) == 4)
# # print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# # print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# # print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# # print(odd_fellow([0, 0, 0]) == 0)

# #Data Structures
# - set to get unique values for count
# - list to get all the counts of from the list with distinct values

# #Algo
# def something(parameter):
#     1. find all of the unique values and keep them in the set
#     2. from the set get the element value of those values if the count from the list is odd 
#     3. return the result from the filtered in step 2
    
#Code
def odd_fellow(list1):
    new_set = set(list1)
    count_list = [number for number in new_set if list1.count(number) % 2 == 1]
    return count_list[0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)