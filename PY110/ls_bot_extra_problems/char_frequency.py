# #Problem
# -Input
#     -string text
# -Output
#     - returns a dictionary
#         - keys are unique characters (uppper and lower cases are the same)
#         - number of times character appear in string
# -Explicit Rules
#     -Spaces are to be ignored
#     -keys are lowercase
#     -needs to handle empty string
#     - sort dictionary by descending order, then by keys in ascending order if there is tie
# -Implicit Rules


# #Examples

# # # Test cases
# # print(char_frequency("Hello World") == {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
# # print(char_frequency("aAaaBbbCcc") == {'a': 4, 'b': 3, 'c': 3})
# # print(char_frequency("") == {})
# # print(char_frequency("AbCdEfG") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})

# #Data Structures
# -dictionary comprehension to get count; set to get the unique characters

# #Algo
# 1. remove lower case and remove all punctuation
# 2. convert the function into dictionary
# 3. sort the dictionary by descending order and ascending order for keys when tie
# 4. return the dictionary

#Code
def descending_by_value(item):
    return -item[1], item[0] 

def char_frequency(text):
    if not text:
        return {}
    formatted_string = text.lower().replace(' ','')
    unique_character_set = sorted(set(formatted_string))
    resulting_dictionary = {char: formatted_string.count(char) for char in unique_character_set}
    final_dict = dict(sorted(resulting_dictionary.items(), key=descending_by_value))
    return final_dict


# Test cases

# Updated test cases 
print(char_frequency("Hello World") == {'l': 3, 'o': 2, 'd': 1, 'e': 1, 'h': 1, 'r': 1, 'w': 1}) 
print(char_frequency("aAaaBbbCcc") == {'a': 4, 'b': 3, 'c': 3}) 
print(char_frequency("") == {}) 
print(char_frequency("AbCdEfG") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}) 