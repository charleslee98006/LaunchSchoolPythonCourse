#Problem
# Input:
#     - non-empty string
# Output:
#     - return integer longest vowel substring length
# Explicit Rules:
#     - String will always have a character
#     - Input is all lower case alphabet
#     - aeiou are vowels
# Implicit Rules:
#     - characters are to be connected with each other
# Question:
#     - 
# #Examples

# print(longest_vowel_substring('cwm') == 0)
# print(longest_vowel_substring('many') == 1)
# print(longest_vowel_substring('launchschoolstudents') == 2)
# print(longest_vowel_substring('eau') == 3)
# print(longest_vowel_substring('beauteous') == 3)
# print(longest_vowel_substring('sequoia') == 4)
# print(longest_vowel_substring('miaoued') == 5)

# #Data Structures
# - nested lists

# #Algo
# def longest_vowel_substring(parameter):
#     1. get all combinations of letters in a list
#     2. filter out combinations that have consanants
#     3. find the combination with the greatest length
#Code
def longest_vowel_substring(text):
    new_list = [text[index:index2+1] for index in range(len(text)) for index2 in range(index, len(text))]
    # print(new_list)
    filtered_list = []
    for sublist in new_list:
        substring = ''
        for character in sublist:
            if character in 'aeiou':
                substring += character
            else:
                substring = ''
                break
        filtered_list.append(len(substring))
    # print(filtered_list)
    # print(max(filtered_list))
    if(filtered_list):
        # print(max(filtered_list))
        return max(filtered_list)
    return 0

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)