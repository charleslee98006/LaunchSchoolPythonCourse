#Problem
# -Input
#     - string
# -Output
#     - dictionary 
# -Explicit Rules
#     - dictionary key are to be lowercase letters from the string
#     - dictionary value are the number of occurrence of the lowercase letter
# Implicit Rules
#     - Uppercases and special characters do not count
# Questions
#     - what about empty string
    
#Examples

# expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
# print(count_letters('woebegone') == expected)

# expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
#             'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
# print(count_letters('lowercase/uppercase') == expected)

# expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
# print(count_letters('W. E. B. Du Bois') == expected)

# print(count_letters('x') == {'x': 1})
# print(count_letters('') == {})
# print(count_letters('!!!') == {})

#Data Structures
# - set would work to get unique value
#Algo
# def count_letters(text):
#     1. get the set of characters from text in lowercase
#     2. create a empty dictionary called new_dict
#     3. iterate over each character in the set:
#         1. check to see if the character is an alphabet and that the count != 0:
#             1.  if yes, assign the character as key and the count of that character in text
#     4. return new_dict

#Code
def count_letters(text):
    new_set = set(text.lower())
    new_dict = {}
    for character in new_set:
        if character.isalpha() and text.count(character) != 0:
            new_dict[character] = text.count(character)
    return new_dict

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})