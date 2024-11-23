# #Problem
# Input:
#     - two string arguements
# Output:
#     - return the number of occurence the second string is in the first string
# Explicit Rules:
#     - overlapping strings don't count
#     - no empty string for the second arguement
# Implicit Rules:
#     - in order for overlap to occur is when the first and last position are the same
# Question:
#     - 
# #Examples

# print(count_substrings('babab', 'bab') == 1)
# print(count_substrings('babab', 'ba') == 2)
# print(count_substrings('babab', 'b') == 3)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('', 'x') == 0)
# print(count_substrings('bbbaabbbbaab', 'baab') == 2)
# print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
# print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# #Data Structures
# probably not need a list

# #Algo
# def count_substrings(parameter):
#     1. go through each characters based on position
#         1. if there is a match keep track of the last position and increment the count
#         2. if there is a match, but the last position is the same as the first position, don't do anything.
#     return the count 
#Code

def count_substrings(text, target_text):
    # solution 1
    # running_total = 0
    # last_position = -1
    # for index in range(len(text)):
    #     for index2 in range(index, len(text)):
    #         if text[index:index2+1] == target_text and index != last_position:
    #             running_total += 1
    #             last_position = index2
    #             # print(text[index:index2+1])
    #             # print(index)
    #             # print(index2)
    # return running_total
    # new_list = [text[index: index2] for index in range(len(text)) for index2 in range(index+1, len(text)+1)]
    # print(new_list)
    
    # Solution #2
    # new_text = text
    # running_total = 0
    # while target_text in new_text:
    #     print(new_text.index(target_text))
    #     running_total +=1
    #     new_text = new_text.replace(target_text, '', 1)
    #     print(new_text)
    # return running_total

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)