#Problem 
# -Input
#     - string text
# -Output
#     - longest palindrome substring
# -Explicit Rules
#     - palindrome reads the same front and back
# -Implicit Rules
#     - palindrome like a mirror
#     - can return any palindrome in length is equal
#     - must be the longest char string
#     - single character counts
# -Question

#Example

#    # Test case 1: Simple palindrome
#     assert longest_palindrome("babad") in ["bab", "aba"]

#     # Test case 2: Entire string is a palindrome
#     assert longest_palindrome("racecar") == "racecar"

#     # Test case 3: No palindrome
#     assert longest_palindrome("abcd") in ["a", "b", "c", "d"]

#     # Test case 4: Multiple palindromes
#     assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"

#     # Test case 5: Empty string
#     assert longest_palindrome("") == ""

#     # Test case 6: Single character
#     assert longest_palindrome("a") == "a"

#     # Test case 7: Two same characters
#     assert longest_palindrome("aa") == "aa"

#     # Test case 8: Long string with short palindrome
#     assert longest_palindrome("abcdefghijklmnopqrstuvwxyz") in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Data structure
# - list of substrings for all combinations

#Algo
# def longest_palindrome(text):
#     1. get all possible combination substrings in the list based on if their reverse is the same
#     2. return the max length from list

#Code
def longest_palindrome(text):
    new_list = [text[index: index2] for index in range(len(text)) for index2 in range(index+1, len(text)+1)]
    filtered_list = [each for each in new_list if each == each[::-1]]
    result_sort_list = sorted(filtered_list, key=len, reverse=True) 
    if filtered_list:
        return result_sort_list[0]
    return ''
  # Test case 1: Simple palindrome
print(longest_palindrome("babad") in ["bab", "aba"])

# # Test case 2: Entire string is a palindrome
print(longest_palindrome("racecar") == "racecar")

# # Test case 3: No palindrome
print(longest_palindrome("abcd") in ["a", "b", "c", "d"])

# # Test case 4: Multiple palindromes
print(longest_palindrome("forgeeksskeegfor") == "geeksskeeg")

# # Test case 5: Empty string
print(longest_palindrome("") == "")

# # Test case 6: Single character
print(longest_palindrome("a") == "a")

# # Test case 7: Two same characters
print(longest_palindrome("aa") == "aa")

# # Test case 8: Long string with short palindrome
print(longest_palindrome("abcdefghijklmnopqrstuvwxyz") in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
