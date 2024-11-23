# #Problem
# Input:
#     - string arg
# Output:
#     - tuple of string and int
# Explicit Rules:
#     - args consists of lowercase alphabets
#     - fomula => s == t * k
#     - t and k shuld be the shortest substring and largest possible repeat
#     - must satifies the equation
# Implicit Rules:
#     - there won't be any empty string for parameter
    #   - characters by themselves do not count
# Question:
#     - 
#Examples

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))

#Data Structures
# - list combination of all possible substring

# #Algo
# def repeated_substring(parameter):
#     1. get all combination of substrings
#     2. count number the shortest substring with repeats
#     3. return the tuple

#Code
def repeated_substring(text):
    list2 = [text[index: index2] for index in range(len(text)) for index2 in range(index+1, len(text)+1) if len(text) == (len(text[index: index2]) * text.count(text[index: index2]))]
    # print(list2)
    min_substring = min(list2)
    return (min_substring, text.count(min_substring))

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))