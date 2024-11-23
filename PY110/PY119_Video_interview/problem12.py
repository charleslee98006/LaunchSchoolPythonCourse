# #Problem
# Input:
#     - string text
# Output:
#     - boolean True if pangram
#     - boolean False if not
# Explicit Rules:
#     - every letter of the alphabet once
#     - cases sensitivity not matter
# Implicit Rules:
#     - duplicates not a problem
# Question:
#     - 
# #Examples
# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

# #Data Structures
# - dictionary to get every letter and see if there is any occurrence

# #Algo
# def is_pangram(parameter):
    #  1. take the text and sort out the unique characters from the list
    #  2. sort the unique characters into alphebatical order
    #  3. check to see if a to z is in the alphabetically order characters
    
#Code
def is_pangram(text):
    new_list = text.lower().replace(' ', '')
    sorted_list = ''.join(sorted(set(new_list)))
    # print(new_list)
    # print(sorted_list)
    return 'abcdefghijklmnopqrstuvwxyz' in sorted_list


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)