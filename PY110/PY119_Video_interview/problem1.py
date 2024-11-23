#Pedac

#Problem
# Input
#     -List
# Output
#     - resulting list
# Explicit Rules
#     - for each number detemrine how many numbers from list are smaller than and place it in the list
#     - count only unique values
# Implicit Rules
# Questions

# #Example
# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)

# #Data Structure
# -List
# #Algorithm
# def smaller_numbers_than_current(list1):
#     1. Create a variable called new_list ans assign it with an empty list
#     2. iterate through list1 and do the following
#         1. get the first element and assign it to a variable
#         2. Create another list called inner_list
#         3. in another loop, compare the next element to the first element and do the following:
#             1. if value is smaller than the first element and not in inner_list
#                 - add it to the inner_list
#         4. get the sum of the inner_list and add the sum to new_list
#     3. return new_list
    
#Code
def smaller_numbers_than_current(list1):
    new_list = []
    for index in range(len(list1)):
        new_inner_list = []
        for index2 in range(len(list1)):
            if(list1[index] > list1[index2] and list1[index2] not in new_inner_list):
                new_inner_list.append(list1[index2]) 
        new_list.append(len(new_inner_list))
    return(new_list)

    # return [sum([1 for number in list1 if number < each]) for each in list1]   


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
