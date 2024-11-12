#P
# Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. 
# A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

# input - string text
# output - boolean True or False
# Explicit Rules
#     - A palindrome reads the same forwards and backwards
#     - Case matters
#     - Character matters
# Implicit Rules:
#     - can't really think of one. Pretty straight forward
# Questions
    # - How are we to treat empty strings? and single character?

#E
# All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

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
def is_palindrome(text):
    for index in range(0, len(text)):
        if(text[index] != text[-1-index]):
            return False
    return True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)