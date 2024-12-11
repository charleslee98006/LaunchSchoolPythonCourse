#Problem
# -Input
#     -List of integer
# -Output
#     - return the longest length consecutive elements sequence
# -Explicit Rules
#     - Consecutive elements meaning numbers after each other 1,2,3,4,5, etc.
# -Implicit Rules
#     - Only count once for duplicates

#Examples

# # Test case 1: Simple sequence
# print("Test case 1:")
# result = longest_consecutive([100, 4, 200, 1, 3, 2])
# print(f"Input: [100, 4, 200, 1, 3, 2]")
# print(f"Expected: 4")
# print(f"Got: {result}")
# print("Passed" if result == 4 else "Failed")
# print()

# # Test case 2: No sequence
# print("Test case 2:")
# result = longest_consecutive([5, 10, 15, 20])
# print(f"Input: [5, 10, 15, 20]")
# print(f"Expected: 1")
# print(f"Got: {result}")
# print("Passed" if result == 1 else "Failed")
# print()

# # Test case 3: Empty list
# print("Test case 3:")
# result = longest_consecutive([])
# print(f"Input: []")
# print(f"Expected: 0")
# print(f"Got: {result}")
# print("Passed" if result == 0 else "Failed")
# print()

# # Test case 4: All consecutive
# print("Test case 4:")
# result = longest_consecutive([1, 2, 3, 4, 5])
# print(f"Input: [1, 2, 3, 4, 5]")
# print(f"Expected: 5")
# print(f"Got: {result}")
# print("Passed" if result == 5 else "Failed")
# print()

# # Test case 5: Duplicate numbers
# print("Test case 5:")
# result = longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# print(f"Input: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]")
# print(f"Expected: 9")
# print(f"Got: {result}")
# print("Passed" if result == 9 else "Failed")
# print()



#Data Structure
# -list to sort all of the consecutive length

# #Algo
# def longest_consecutive(lst):
#     1. Sort the list in ascending order
#     2. create a counter = 1
#     3. check if the first number and the second number are consecutive
#         1. if yes, increment counter by 1
#         2. if equal to each other, don't do anything
#         2. if less, save the value and reset counter to zero
#         3. repeat step 3 above, but with second number and third number and so on so forth
#     4. return the counter
    
#Code
def longest_consecutive(lst):
    if not lst:
        return 0
    ascending_list = sorted(lst)
    counter = 1
    # print(ascending_list)
    filtered_list = []
    for index in range(len(ascending_list)-1):
        if ascending_list[index] + 1 == ascending_list[index + 1]:
            counter += 1
        elif ascending_list[index] + 1 < ascending_list[index + 1]:
            counter = 1
        filtered_list.append(counter)
    # print(filtered_list)
    return max(filtered_list)

# Test case 1: Simple sequence
print("Test case 1:")
result = longest_consecutive([100, 4, 200, 1, 3, 2])
print(f"Input: [100, 4, 200, 1, 3, 2]")
print(f"Expected: 4")
print(f"Got: {result}")
print("Passed" if result == 4 else "Failed")
print()

# Test case 2: No sequence
print("Test case 2:")
result = longest_consecutive([5, 10, 15, 20])
print(f"Input: [5, 10, 15, 20]")
print(f"Expected: 1")
print(f"Got: {result}")
print("Passed" if result == 1 else "Failed")
print()

# Test case 3: Empty list
print("Test case 3:")
result = longest_consecutive([])
print(f"Input: []")
print(f"Expected: 0")
print(f"Got: {result}")
print("Passed" if result == 0 else "Failed")
print()

# Test case 4: All consecutive
print("Test case 4:")
result = longest_consecutive([1, 2, 3, 4, 5])
print(f"Input: [1, 2, 3, 4, 5]")
print(f"Expected: 5")
print(f"Got: {result}")
print("Passed" if result == 5 else "Failed")
print()

# Test case 5: Duplicate numbers
print("Test case 5:")
result = longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(f"Input: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]")
print(f"Expected: 9")
print(f"Got: {result}")
print("Passed" if result == 9 else "Failed")
print()