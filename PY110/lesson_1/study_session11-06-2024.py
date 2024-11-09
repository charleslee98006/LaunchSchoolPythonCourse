# /*
# Difference of Two
# The objective is to return all pairs of numbers from a given array of numbers that have a difference of 2.
# The result array should be sorted in ascending order of values.
# Assume there are no duplicate numbers in the array.
# The order of the numbers in the input array should not matter.
# */

# P
#     Input:
#         - list of numbers 
# #     Output: 
#         - Nest of pair values
# #     Explicit Rules:
# #         - Assume No dups in input array
# #         - Input array order does not matter
#           - return pairs of values from array with difference of 2
# #     Implicit Rules:
#         - Nested arrays list pair within a list
#         - What about the case of empty? What about the case of 1 number?
# E
#  See below
# D
# Seems like lists are to be used given from the output
# A



# difference_of_two function:
#   1. Create an empty list
#   2. find the pairs from the array 
#      -  (look at Helper function)
#   3. place the pairs in the empty list
#   4. return the list  
# find_the_difference function:
#   1. create new list
#   2.  check the element 1 and element 2 and see if the difference is 2
#        - if yes, add to the new list
#        - if no, go onto the next comparison
#   3. Repeat step 3, but check element 1 and element 3 and so on and so forth.
#        - stop when there is no more elements to comparion
#   4. return the list
# C

def difference_Of_Two(int_array):
    result_list = []
    index_position1 = 0
    index_position2 = 1
    while index_position1 < len(int_array):
        is_pair = is_difference_by_two(int_array[index_position1], int_array[index_position2])
        if(is_pair):
            result_list.append(pair)
        if(index_position2 == len(int_array)):
            index_position1 += 1
            index_position2 = index_position1 + 1
        else:
                
    return list(result_list)
    
def is_difference_by_two(element1, element2):
    return True if(abs(element1 - element2) == 2) else: False
    
# // Test cases
# print(differenceOfTwo([1, 2, 3, 4]));
# // [[1, 3], [2, 4]]
# print(differenceOfTwo([4, 1, 2, 3]));
# // [[1, 3], [2, 4]]
# print(differenceOfTwo([1, 23, 3, 4, 7]));
# //  [[1, 3]]
# print(differenceOfTwo([4, 3, 1, 5, 6]));
# // [[1, 3], [3, 5], [4, 6]]
# print(differenceOfTwo([2, 4]));
# // [[2, 4]]
# print(differenceOfTwo([1, 4, 7, 10, 13]));
# // []