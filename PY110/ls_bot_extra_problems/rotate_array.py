# #Problem
# -Input
#     - int list nums
#     - int k number of step to rotate
# -Output
#     - list from rotation
# -Explicit R
#     - values from the back go to the front
#     -
# -Implicit R
#     - order does matter
#     - steps can be greater than the len of list

# #Example

# # Test cases
# # print(rotate_array([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4])
# # print(rotate_array([-1,-100,3,99], 2) == [3,99,-1,-100])
# # print(rotate_array([1,2], 3) == [2,1])
# # print(rotate_array([1], 0) == [1])
# # print(rotate_array([], 1) == [])
# # print(rotate_array([1,2,3], 4) == [3,1,2]) => [3,1,2]=>[2,3,1]=>[1,2,3]   =>[3,1,2]=> 1

# #Data Structure
# -lists

# #Algo
# 1. find the position from the right to start the slice
# 2. take the slice from that position to the end and add the left over to the back of the slice
# 3. return the result

#Code
def rotate_array(nums_list, nums_rotation):
    if not nums_list:
        return []
    elif len(nums_list) == 1:
        return nums_list
    start = len(nums_list) - (nums_rotation % len(nums_list))
    #slicing solution:
    # return nums_list[start:] + nums_list[:start]

    # O(1) space solution
    for index in range(start, len(nums_list)):
        temp = nums_list[index - start]
        nums_list[index - start] = nums_list[index]
        nums_list[index] = temp
    if(len(nums_list) % 2 == 1):
        value = nums_list.pop(len(nums_list) // 2)
        nums_list.append(value)
    return nums_list


# Test cases
print(rotate_array([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4])
print(rotate_array([-1,-100,3,99], 2) == [3,99,-1,-100])
print(rotate_array([1,2], 3) == [2,1])
print(rotate_array([1], 0) == [1])
print(rotate_array([], 1) == [])