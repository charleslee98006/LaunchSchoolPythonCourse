# #Problem
# - Input
#     - string text
# - Output
#     - returns the first occurence of the greatest count
# - Explicit Rules
#     - uppercase and lowercase are the same
# - Implicit Rules
# - Questions

# #Example
# # print(most_common_char('Hello World') == 'l')
# # print(most_common_char('Mississippi') == 'i')
# # print(most_common_char('Happy birthday!') == 'h')
# # print(most_common_char('aaaaaAAAA') == 'a')

# # my_str = 'Peter Piper picked a peck of pickled peppers.'
# # print(most_common_char(my_str) == 'p')

# # my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# # print(most_common_char(my_str) == 'e')


# #Data Structure
# - set to get the distinct characters

# #Algo
# def most_common_char(text):
#     1. get a copy of the text in lowercase and convert it into a set and assign it to new_set
#     2. create a variable called max_occurrence_char and give it an empty string
#     3. create a variable called max_occurrence_based_on_char and give it a 0
#     2. using the characters in new_set, do the following:
#         1. compare the max_occurrence_based_on_char and the character occurrence from text
#             if character occurrence is bigger
#                 set max_occurrence_based_on_char to character occurrence and max_occurrence_char to the character
#     3. return max_occurrence_char  

#Code
def most_common_char(text):
    new_dict = {}
    for character in text.lower():
        count = new_dict.get(character, 0)
        new_dict[character] = count + 1
    max_count = 0
    max_count_key = ''
    for key, value in new_dict.items():
        if value > max_count:
            max_count = value
            max_count_key = key
    return max_count_key


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')