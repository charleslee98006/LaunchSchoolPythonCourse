# #Problem
# Input:
#     - string of digits
# Output:
#     - return the number of even numbered sub strings
# Explicit Rules:
#     - if substring shows up more than 1 time, it will count.
# Implicit Rules:
#     -
# Question:
#     - 
# #Examples

# # print(even_substrings('1432') == 6)
# # print(even_substrings('3145926') == 16)
# # print(even_substrings('2718281') == 16)
# # print(even_substrings('13579') == 0)
# # print(even_substrings('143232') == 12)

# #Data Structures
# - list of all even-numbered combinations

# #Algo
# def even_substrings(parameter):
#     1. get a list of all even numbers from the digit string
#     2. get all the combinations from the list in step1
#     3. count all of the combo and return the count
#Code
def even_substrings(digit_text):
    list1 = [ digit_text[index:index2+1] for index in range(len(digit_text)) for index2 in range(index, len(digit_text))if int(digit_text[index:index2+1]) % 2 == 0]
    return len(list1)
    


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)