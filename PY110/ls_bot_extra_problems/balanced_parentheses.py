# #Problem
# -Input
#     - string text
# -Output
#     - Boolean True if balanced; False otherwise
# -Explicit Rules
#     - Balanced means that parenthesis has corresponding opening and closing brackets
# -Implicit Rules

# #Examples

# # print(balanced_parentheses("()") == True)
# # print(balanced_parentheses("((()))") == True)
# # print(balanced_parentheses("(()())") == True)
# # print(balanced_parentheses("(())()") == True)
# # print(balanced_parentheses("(()(()))") == True)
# # print(balanced_parentheses("(") == False)
# # print(balanced_parentheses(")") == False)
# # print(balanced_parentheses(")(") == False)
# # print(balanced_parentheses("(()") == False)
# # print(balanced_parentheses("())") == False)
# # print(balanced_parentheses("((())") == False)
# # print(balanced_parentheses("())(()") == False)
# # print(balanced_parentheses("") == True)
# # print(balanced_parentheses("(hello)") == True)
# # print(balanced_parentheses("(hello(world))") == True)
# # print(balanced_parentheses("((hello)(world))") == True)
# # print(balanced_parentheses("(hello)(world)") == True)
# # print(balanced_parentheses("(hello(world)") == False)

# #Data Structures
# -We can go with stack using a list

# #Algo
# def balanced_parentheses(text):
#     1. create an empty list and call it `stack`
#     2. go through each character and do the following:
#         1. if there is an open parentheses, append it to the `stack`
#         2. if closing parentheses, 
#             1. Check to see if there is any element in stack, if not, return False, else pop the `stack`
#     3. return False if stack still has elements, else True
#Code
def balanced_parentheses(text):
    stack = []
    for character in text:
        if character == '(':
            stack.append(character)
        elif character == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(balanced_parentheses("()") == True)
print(balanced_parentheses("((()))") == True)
print(balanced_parentheses("(()())") == True)
print(balanced_parentheses("(())()") == True)
print(balanced_parentheses("(()(()))") == True)
print(balanced_parentheses("(") == False)
print(balanced_parentheses(")") == False)
print(balanced_parentheses(")(") == False)
print(balanced_parentheses("(()") == False)
print(balanced_parentheses("())") == False)
print(balanced_parentheses("((())") == False)
print(balanced_parentheses("())(()") == False)
print(balanced_parentheses("") == True)
print(balanced_parentheses("(hello)") == True)
print(balanced_parentheses("(hello(world))") == True)
print(balanced_parentheses("((hello)(world))") == True)
print(balanced_parentheses("(hello)(world)") == True)
print(balanced_parentheses("(hello(world)") == False)