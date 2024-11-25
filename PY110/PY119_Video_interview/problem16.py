# #Problem
# Input:
#     - string of alphanumeric text
# Output:
#     - count of distinct case insensitive alphebetical and numerical characters occur more than once
# Explicit Rules:
#     -only alphanumeric characters
#     - case don't matter
# Implicit Rules:
#     - check to see if characters show up more than once
# Question:
#     - 
# #Examples
# # print(distinct_multiples('xyz') == 0)               # (none)
# # print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# # print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# # print(distinct_multiples('unununium') == 2)         # u, n
# # print(distinct_multiples('multiplicity') == 3)      # l, t, i
# # print(distinct_multiples('7657') == 1)              # 7
# # print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# # print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# #Data Structures
# set to get all of the distinct characters


# #Algo
# def distinct_multiples(parameter):
#     1. get the distinct characters from the text
#     2. for the distinct characters, get how many times those characters appear more than once
#     3. tally up the duplicates and return the tally
    
#Code
def distinct_multiples(text):
    # something = set(list(text.lower()))
    # print(something)
    new_list = [1 if text.lower().count(character) >= 2 else 0 for character in set(list(text.lower())) ]
    # print(new_list)
    return sum(new_list)
    
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5


