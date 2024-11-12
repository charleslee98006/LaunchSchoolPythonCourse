# target_letters = ['a', 'b', 'c', 'd', 'e']
# characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

# new_dict = {letter: {'present': characters.count(letter) > 0, 'count': characters.count(letter)} for character in characters for letter in target_letters }

# print(new_dict)
# # {
# #     'a': { 'present': True, 'count': 1 },
# #     'b': { 'present': True, 'count': 2 },
# #     'c': { 'present': False, 'count': 0 },
# #     'd': { 'present': True, 'count': 1 },
# #     'e': { 'present': False, 'count': 0 },
# # }


# Remove all duplicate letters from a string, keeping only the first occurrence.
# The input is restricted to contain no numerals and only words containing the English alphabet letters.

# You may not use a set.

def remove_duplicates(string):
    string_lower_checker = ''
    new_string = ''
    for char in string:
        if char.lower() not in string_lower_checker:
            new_string += char
            string_lower_checker += char.lower()
    return new_string

# Tests
print(remove_duplicates("Launch School") == "Launch So")
print(remove_duplicates("CodeWars can't Load Today") == "CodeWars n'tLy")
print(remove_duplicates("success") == "suce")

# #P
# Input:
#     - string text
# Output:
#     - removing dups from string keeping first occurrence only
# Explicit Rules:
#     - keep first occurrence only
#     - no numbers
#     - only english alphabets letters
# Implicit Rules:
#     - iterating throughout the string from beginning to end
#     - keeping the first 
# Question:
#     - 
# #E
# # print(remove_duplicates("Launch School"))
# # print(remove_duplicates("Launch School") == "Launch So")
# # print(remove_duplicates("CodeWars can't Load Today") == "CodeWars n'tLy")
# # print(remove_duplicates("success") == "suce")

# #D
# -

# #A
# def something(parameter):
#     1.
# #C