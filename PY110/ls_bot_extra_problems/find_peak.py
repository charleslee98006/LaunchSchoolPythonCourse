# #problem
# -Input
#     - list of integers
# -Output
#     - index of a peak element
# -Explicit Rules
#     - multiple peaks return any one of the peaks
#     - peak is the local or global maxs
#     - if none, return -1
#     - first element is peak if greater than element to the its right
#     - last element is peak if greater than lemene to its left
# -Implicit Rules
#     - order does matter

# #Examples

# # # Test cases
# # print(find_peak([1, 3, 20, 4, 1, 0]) in [2])  # Should return True (index 2 is a peak)
# # print(find_peak([5, 2, 3, 1]) in [0, 2])  # Should return True (indices 0 and 2 are peaks)
# # print(find_peak([1, 2, 3, 4, 5]) in [4])  # Should return True (index 4 is a peak)
# # print(find_peak([5, 4, 3, 2, 1]) in [0])  # Should return True (index 0 is a peak)
# # print(find_peak([1, 1, 1, 1]) == -1)  # Should return True (no peak)

# #Data Structures
# -Not really

# #Algo
# def find_peak(number_list):
#     1. get the index of the max value from list
#     2. return the index


#Code
def find_peak(number_list):
    if(any(element != max(number_list) for element in number_list)):
        return number_list.index(max(number_list))
    return -1

# Test cases
print(find_peak([1, 3, 20, 4, 1, 0]) in [2])  # Should return True (index 2 is a peak)
print(find_peak([5, 2, 3, 1]) in [0, 2])  # Should return True (indices 0 and 2 are peaks)
print(find_peak([1, 2, 3, 4, 5]) in [4])  # Should return True (index 4 is a peak)
print(find_peak([5, 4, 3, 2, 1]) in [0])  # Should return True (index 0 is a peak)
print(find_peak([1, 1, 1, 1]) == -1)  # Should return True (no peak)