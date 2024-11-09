#P
# In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. 
# In this exercise and the next, you're going to reverse those functions.
# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.
# You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.
# Input:
#     - non-negative integer value
# Output:
#     - string version of non-negative integer
# Explicit Rules:
#     - no using any Python standard libs
# Implicit Rules:
#     - will need to do some string number mapping
#E
# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

#D
# - we can use a dictionary and map the numbers to numerical values.

#A
# def integer_to_string(number):
#     1. create a dictionary with key are integer and values string number
#     2. set exponent argument to 1
#     3. create a new empty string
#     4. in a loop where number is greater or than -1, do the following:
#         1. get the remainder by divided number by 10 to the exponent argument
#         2. subtract the number by the remainder multipled by 10 to the exponent
#         2. get the string value of the resulting number from the dictionary 
#         3. add string value to the new string
#         4. increment the exponential arg by 1
#     5. return the new string
#C
def integer_to_string(number):
    STRING_NUM_MAPPING = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 0:'0'}
    exponent_arg = 1
    result_string = ''
    if(number):
        while(number > 0):
            remainder = number % 10**exponent_arg
            # print(remainder)
            number -= remainder
            string_version = STRING_NUM_MAPPING.get(remainder // 10**(exponent_arg-1))
            exponent_arg += 1
            result_string += string_version
        return result_string[::-1]
    return '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True