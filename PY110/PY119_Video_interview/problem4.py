# #Problem

# -Input
#     -list of integers
# -Output
#     - tuple of two numbers closest together by value
# -Explicit Rules
#     - if multiple pairs are equally close, return first occurence
# -Implicit Rules

# -Questions

# #Example
# # print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# # print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# # print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# #Data Structure
# - list
# #Algo
# def closest_number(list1):
#     1. create an empty list and assigned it to new_list
#     2. iterate over list1 by index and do the following:
#         1. create an empty list and assign it to new_inner_list
#         2. iterate over list1 but with index+1 and do the following:
#             1.  store the index and second index and the difference in new_inner_list
#     3. find the min from new_list and get the two index
#     4. return the two index in tuple form
        
#Code
def distance(list):
    return list[2]

def closest_numbers(list1):
    new_list = []
    for index in range(len(list1)):
        for index2 in range(index + 1, len(list1)):
            new_inner_list = []
            new_inner_list.extend([index, index2, abs(list1[index]-list1[index2])])
            new_list.append(new_inner_list)
    final_list = sorted(new_list, key=distance)
    return (list1[final_list[0][0]], list1[final_list[0][1]])

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))