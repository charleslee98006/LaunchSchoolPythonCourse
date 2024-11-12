#P
# Write a function that takes a list of positive integers as input, multiplies all of the integers together, 
# divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.
#

# Input:
#     - list of positive ints
# Output:
#     - return as string with 3 decimal places
# Explicit Rules:
#     - multiple all the integer together
#     - divide the result by number length of the list
#     - round to 3 decimal places
# Implicit Rules:
#     - we must use the value of 1 or else if zero, everything will still be zero.
# Question:
#     - 
#E

# # All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

#D
# - none needed

#A
# def multiplicative_average(list):
#     1. Create a veriable titled `multiplication_result` with the value of 1
#     2. in a loop, iterate through the list and do the following:
#         1. multiply each value with the multiplication_result
#         2. add the multiplied value to the multiplication_result
#     3. divide the multiplication_result by the length of the list
#     5. return the final form with the format the result from step 3 to 3 decimal places as a string
#C
def multiplicative_average(list):
    multiplcative_result = 1
    for number in list:
        multiplcative_result *= number
    return f'{multiplcative_result / len(list):.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")