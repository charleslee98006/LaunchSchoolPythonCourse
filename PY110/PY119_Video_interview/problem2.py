#WTF....

# #P
# Input
# - list of integers
# Output
# - returns integer of the min sum of 5 numbers or None
# Explicit Rules
# - returns integer of the min sum of 5 numbers
# - if list is less than 5 return none

# Implicit Rules

# Questions

# #Example
# print(minimum_sum([1, 2, 3, 4]) is None)
# print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
# print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
# print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
# print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
# #Data Structures
# -List

# #Algo
# def minimum_sum(list1):
#     1. check to see if list1 is less than 5
#         if yes, return None
#     2. sort list1 in ascending order
#     3. get sum of the first 5 elements from list1
#     4. return the sum

#Code
def minimum_sum(list1):
    if(len(list1) < 5):
        return None
    new_list = []
    counter = 0
    while counter + 5 <= len(list1):
        new_list.append(list1[counter: counter + 5])
        counter += 1
    # print(new_list)
    # print([sum(sublist) for sublist in new_list])
    return min([sum(sublist) for sublist in new_list])
        
    # for index in range(len(list1)):
    #     new_inner_list = []
    #     for index2 in range(index+1,len(list1)):
    #         new_inner_list.append(list1[index:index2+1])
    #     new_list.append(new_inner_list)
    # filter_list = [sublist for each in new_list for sublist in each if len(sublist) == 5]
    # sum_filter_list = [sum(sublist) for each in new_list for sublist in each if len(sublist) == 5]
    # print(filter_list)
    # print(sum_filter_list)


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)