#Problem
# - Input
#     - unsorted integer list
# -Output
#     - find the length of longest sequence of numbers from list
# -Explicit Rules
# -Implicit Rules

# #Examples

# # # Test cases
# # print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4)
# # print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
# # print(longest_consecutive_sequence([]) == 0)
# # print(longest_consecutive_sequence([1, 2, 0, 1]) == 3)
# # print(longest_consecutive_sequence([1, 1, 1, 2, 2, 3]) == 3)

# #DS
# - set to get unique values and remove dups
# - list of sorted set
# #Algo
# def longest_consecutive_sequence(list1):
#     1. sort and get the set of unique values in ascending order
#     2. create a variable called `placeholder` and equal it to 0
#     3. create a variable called `new_list` with an empty list
#     2. check the first and second element and see if they are off by 1
#         if not - slice the list and reset the placeholder to the second element's position 

    
#Code
def longest_consecutive_sequence(list1):
    if not list1:
        return 0
    # sorted_list = sorted(set(list1))  # Remove duplicates and sort
    # new_list = []
    # placeholder1 = 0
    # placeholder2 = 0
    # while placeholder2 < len(sorted_list):
    #     if placeholder2 == len(sorted_list) - 1 or sorted_list[placeholder2 + 1] - sorted_list[placeholder2] != 1:
    #         new_list.append(sorted_list[placeholder1:placeholder2 + 1])
    #         placeholder1 = placeholder2 + 1
    #         # print('new_list: ', new_list)
    #     placeholder2 += 1
    # # print(new_list)
    # return max(len(seq) for seq in new_list)
    
    max_length = 0
    num_set = set(list1)
    # print(num_set)
    for number in num_set:
        print(number)
        if number -1 not in num_set:
            current_num = number
            current_length = 1
            while (current_num + 1 in num_set):
                current_num +=1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length

# Test cases
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4)
# print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
# print(longest_consecutive_sequence([]) == 0)
# print(longest_consecutive_sequence([1, 2, 0, 1]) == 3)
# print(longest_consecutive_sequence([1, 1, 1, 2, 2, 3]) == 3)