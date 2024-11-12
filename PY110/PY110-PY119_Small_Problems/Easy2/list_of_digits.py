#P
# Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

# Input:
#     - positive integer
# Output:
#     - list of digits for the int
# Explicit Rules:
#     -
# Implicit Rules:
#     -
# Question:
#     - 
# #E


# #D


# #A
# def something(parameter):
#     1.
# #C
def digit_list(number):
    return  [int(nums) for nums in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True