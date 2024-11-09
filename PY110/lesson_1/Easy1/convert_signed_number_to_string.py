#P
# In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.
# Input:
#     - non-negative integer value
# Output:
#     - string version of non-negative integer
# Explicit Rules:
#     - no using any Python standard libs
# Implicit Rules:
#     - will need to do some string number mapping
#E
# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True

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
def signed_integer_to_string(number):
    sign = '+' 
    if number < 0:
        sign = '-'
        number = abs(number)
    STRING_NUM_MAPPING = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 0:'0'}
    exponent_arg = 1
    result_string = ''
    if(number):
        while(number > 0):
            remainder = number % 10**exponent_arg
            number -= remainder
            string_version = STRING_NUM_MAPPING.get(remainder // 10**(exponent_arg-1))
            exponent_arg += 1
            result_string += string_version
        result_string += sign 
        return result_string[::-1]
    return '0'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True