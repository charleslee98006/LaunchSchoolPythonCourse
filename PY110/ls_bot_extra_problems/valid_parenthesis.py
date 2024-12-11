#problem
# - Input
#     - string text
# - Ouput
#     - boolean True - if input is valid; otherwise false
# -Explicit Rules
#     - brackets needs to be closed by same kind of brackets
#     - order matters
# -Implicit Rules

#examples

# # Test case 1: Valid parentheses
# print("Test case 1:")
# result = is_valid_parentheses("()")
# print(f"Input: '()'")
# print(f"Expected: True")
# print(f"Got: {result}")
# print("Passed" if result == True else "Failed")
# print()

# # Test case 2: Valid mixed brackets
# print("Test case 2:")
# result = is_valid_parentheses("()[]{}")
# print(f"Input: '()[]{}'")
# print(f"Expected: True")
# print(f"Got: {result}")
# print("Passed" if result == True else "Failed")
# print()

# # Test case 3: Invalid closing order
# print("Test case 3:")
# result = is_valid_parentheses("(]")
# print(f"Input: '(]'")
# print(f"Expected: False")
# print(f"Got: {result}")
# print("Passed" if result == False else "Failed")
# print()

# # Test case 4: Invalid nesting
# print("Test case 4:")
# result = is_valid_parentheses("([)]")
# print(f"Input: '([)]'")
# print(f"Expected: False")
# print(f"Got: {result}")
# print("Passed" if result == False else "Failed")
# print()

# # Test case 5: Complex valid nesting
# print("Test case 5:")
# result = is_valid_parentheses("{[]}")
# print(f"Input: '{{[]}}'")
# print(f"Expected: True")
# print(f"Got: {result}")
# print("Passed" if result == True else "Failed")
# print()

#data structures
# - Reminds me of the stack implementation using a list

#algo
# def is_valid_parenthesis(text):
#     1. create a empty list called stack
#     2. iterate over the string text and do the following:
#         1. if open brackets, push them to stack
#         2. if closing brackets, pop from the stack:
#             - if top stack does not matches, return False
#             - if stack is empty return False
#     3. check to see if stack still has elements, return false if it does

#code
def is_valid_parentheses(text):
    stack = []
    for character in text:
        if character in '[({':
            stack.append(character)
        elif len(stack) == 0:
            return False
        elif stack[-1] + character == '()' or stack[-1] + character == '{}' or stack[-1] + character == '[]':
            stack.pop(-1)
        else:
            return False    
    if stack:
        return False
    return True

# Test case 1: Valid parentheses
print("Test case 1:")
result = is_valid_parentheses("()")
print(f"Input: '()'")
print(f"Expected: True")
print(f"Got: {result}")
print("Passed" if result == True else "Failed")
print()

# Test case 2: Valid mixed brackets
print("Test case 2:")
result = is_valid_parentheses("()[]{}")
print(f"Input: '()[]{{}}'")
print(f"Expected: True")
print(f"Got: {result}")
print("Passed" if result == True else "Failed")
print()

# Test case 3: Invalid closing order
print("Test case 3:")
result = is_valid_parentheses("(]")
print(f"Input: '(]'")
print(f"Expected: False")
print(f"Got: {result}")
print("Passed" if result == False else "Failed")
print()

# Test case 4: Invalid nesting
print("Test case 4:")
result = is_valid_parentheses("([)]")
print(f"Input: '([)]'")
print(f"Expected: False")
print(f"Got: {result}")
print("Passed" if result == False else "Failed")
print()

# Test case 5: Complex valid nesting
print("Test case 5:")
result = is_valid_parentheses("{[]}")
print(f"Input: '{{[]}}'")
print(f"Expected: True")
print(f"Got: {result}")
print("Passed" if result == True else "Failed")
print()