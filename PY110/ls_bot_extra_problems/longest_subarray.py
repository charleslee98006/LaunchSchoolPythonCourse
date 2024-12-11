# #Problem
# -Input
#     -int list
#     - max sum k
# -Output
#     -length of the longest subarray of consecutive elements that is <= k
# -Explicit Rules
#     - Consecutive elements are adjust to each other based on the index posiitions
#     - sum of consecutive elements <= k
# -Implicit Rules
#     -Order does matter

# #Examples
# # Test cases
# # print(longest_subarray([1, 2, 3, 4, 5], 9) == 4)  # [1, 2, 3, 3]
# # print(longest_subarray([3, 1, 2, 1], 4) == 3)  # [1, 2, 1]
# # print(longest_subarray([1, 1, 1, 3], 3) == 3)  # [1, 1, 1]
# # print(longest_subarray([2, 2, 2], 1) == 0)  # No subarray possible
# # print(longest_subarray([], 5) == 0)  # Empty input array

# #Data structure
# - nested list to get all combinations of
# #Algo
# def longest_subarray(nums, k):
#     1. get all combinations from nums that are less than k using slices
#     2. get the max length from step 1
#     3. return the max length
    
#code
def longest_subarray(nums, k):
    combo_list = [len(nums[index:index2]) for index in range(len(nums)) for index2 in range(index + 1, len(nums) + 1) if sum(nums[index:index2]) <= k]
    if (combo_list):
        return max(combo_list)
    return 0
# Test cases
print(longest_subarray([1, 2, 3, 4, 5], 9) == 3)  # [1, 2, 3]
print(longest_subarray([3, 1, 2, 1], 4) == 3)  # [1, 2, 1]
print(longest_subarray([1, 1, 1, 3], 3) == 3)  # [1, 1, 1]
print(longest_subarray([2, 2, 2], 1) == 0)  # No subarray possible
print(longest_subarray([], 5) == 0)  # Empty input array