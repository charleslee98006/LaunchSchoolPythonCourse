#P
# Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. 
# To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
# Input:
#     - string text input with parenthesis
# Output:
#     -boolean true or false if parenthesis are balanced and match
# Explicit Rules:
#     - left and right parenthesis must be match
#     - must start with left parenthesis and end with right parenthesis
# Implicit Rules:
#     -
# Question:
#     - 
#E
# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True

#D


#A
# def is_balanced(text):
#     1. create a variable called left pointer
#     2. create a variable called right pointer
#     3. in a loop iterate through the text and do the following:
#         check to see if the character is '(' or ')'
#             - if ')' return false
#             - if '('
#                 in a loop, iterate from  the position of ''

def is_balanced(text):
    pos_left_parenth_list = []
    pos_right_paren_list = []
    for index_post in range(0,len(text)):
        if text[index_post] == '(':
            pos_left_parenth_list.append(index_post)
        elif text[index_post] == ')':
            pos_right_paren_list.append(index_post)
    if(len(pos_left_parenth_list) < len(pos_right_paren_list) 
       or len(pos_left_parenth_list) > len(pos_right_paren_list)):
        return False
    for index in range(0, len(pos_left_parenth_list)):
        if( pos_right_paren_list[index] < pos_left_parenth_list[index]):
            return False
    return True

#C

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True