#P
# Write a function that takes a string of digits and returns the appropriate number as an integer. 
# You may not use any of the standard conversion functions available in Python, such as int. 
# Your function should calculate the result by using the characters in the string.
# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.
# Input:
#     - string of digits
# Output:
#     - return number as integer
# Explicit Rules:
#     - No using int() or standard conversion functions in Python
#     - No need to worry about signage or any invalid characters
#     - all characters are numbers
# Implicit Rules:
#     - digits position will matter
#     - 1, 10, 100, 1000... 10^n patterns will matter.
#     - will need to map numbers from 0 to 9 with the corresponding numbers
#     - No empty strings

#E
# print(string_to_signed_integer("4321") == 4321)  # True 4x10^3 + 3x10^2 + 2x10^1 + 1x10^0
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

#D
# - No needed will be need; we will need a running total

#A
# def string_to_signed_integer(text):
#     1.Initial running total will be 0.
#     2.Get the length of the text
#     3. iterate the index position using the range from 0 to length of the text and do the following:
#         1. get the string character based on the index position 
#         2. map the corresponding string character to the integer number
#         3. multiply integer number with 10 to the exponent of length text -1 - index position
#         4. add to the multiplication number to the running total
#     return the running total

#C
def string_to_signed_integer(text):
    signage = '+'
    if text[0] == '-' or text[0] == '+':
        signage = text[0]
        text = text[1:]
    running_total = 0
    for index in range(0, len(text)):
        number = convert_string_to_int(text[index])
        running_total +=(number * 10**(len(text)-1-index))
    if signage == '-':
        running_total = running_total - (running_total*2)
    return running_total
                    
def convert_string_to_int(string_number):
    match (string_number):
        case '0':
            string_number = 0
        case '1':
            string_number = 1
        case '2':
            string_number = 2
        case '3':
            string_number = 3
        case '4':
            string_number = 4
        case '5':
            string_number = 5
        case '6':
            string_number = 6
        case '7':
            string_number = 7
        case '8':
            string_number = 8
        case '9':
            string_number = 9
    return string_number

print(string_to_signed_integer("4321") == 4321)  # True 4x10^3 + 3x10^2 + 2x10^1 + 1x10^0
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True