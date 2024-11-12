#P
# Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. 
# This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. 
# If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

# input - string text
# output - boolean True or False
# Explicit Rules
#     - A palindrome reads the same forwards and backwards
#     - Case not matters, meaning that upper and lower should be treated the same
#     - ignore all non-alphamerics
# Implicit Rules:
#     - reverse should still be the same 
# Questions
    # - How are we to treat empty strings? and single character? non-Alphanumerics?

#E
# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

#Empty string wasn't answered; hence, we are assuming that there will not be empty string.

#D
# Don't think we will need any at this point.
#A
# 1. set is_palindrome boolean to True
# 2. In a loop:
#     - Get the first character and the last character
#     - Compare the two characters
#         - if they do not match, kick out of the loop and return False
#         - if they do match
#             - search the next character and the second to last character (so on and so forth)
#         - if the first and second character are from the same position
#             - kick out of the loop
# 2. return the is_palindrome 

#C
def is_real_palindrome(text):
    for index in range(0, len(text)):
        if(text[index].lower() != text[-1-index].lower() and not text[index].isalnum() and not text[-1-index].isalnum()):
            return False
    return True

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True