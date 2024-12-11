#Problem
# Input:
#     - strings but contains only `{}`, `[]` and `()`
# Output:
#     - True if string is balanced
#     - False if not balanced
# Explicit Rules:
#     -balanced =
#         - no unmatched brackets
#         - inner brackets are also matched as well
# Implicit Rules:
#     -
# Question:
#     - 
#Examples
# # Test case 1: Empty string
# assert is_balanced("") == True

# # Test case 2: Simple balanced parentheses
# assert is_balanced("()") == True

# # Test case 3: Balanced mix of brackets
# assert is_balanced("([{}])") == True

# # Test case 4: Unbalanced - closing bracket missing
# assert is_balanced("([{])") == False

# # Test case 5: Unbalanced - opening bracket missing
# assert is_balanced("([)]") == False

# # Test case 6: Complex balanced expression
# assert is_balanced("({[]})") == True

# # Test case 7: Complex unbalanced expression
# assert is_balanced("([)]{}") == False

# # Test case 8: Balanced with nested structures
# assert is_balanced("(({}[]))") == True

# # Test case 9: Unbalanced nested structures
# assert is_balanced("((({[]}))") == False

# # Test case 10: Only opening brackets
# assert is_balanced("({[") == False

# # Test case 11: Only closing brackets
# assert is_balanced("}])") == False


#Data Structures


#Algo
# def is_balanced(text):
#     1. get the left side character and see if right side has that character
#         2. if yes, move on and repeat step 1 but get the character
#         3. if not, return false
    
#Code

def is_balanced(text):
    new_stack = []
    for character in text:
        # print(character)
        # print(new_stack)
        if character in '[{(':
            new_stack.append(character)
        elif len(new_stack) == 0:
            return False
        elif (new_stack[-1] =='{' and character =='}') or (new_stack[-1] =='(' and character ==')') or (new_stack[-1] =='[' and character ==']'):
            new_stack.pop(-1)
        else:
            return False
    if new_stack:
        return False
    else:
        return True

# Test case 1: Empty string
assert is_balanced("") == True

# Test case 2: Simple balanced parentheses
print(is_balanced("()") == True)

# Test case 3: Balanced mix of brackets
print( is_balanced("([{}])") == True)

# Test case 4: Unbalanced - closing bracket missing
print( is_balanced("([{])") == False)

# Test case 5: Unbalanced - opening bracket missing
print( is_balanced("([)]") == False)

# Test case 6: Complex balanced expression
print( is_balanced("({[]})") == True)

# Test case 7: Complex unbalanced expression
print( is_balanced("([)]{}") == False)

# Test case 8: Balanced with nested structures
print( is_balanced("(({}[]))") == True)

# Test case 9: Unbalanced nested structures
print( is_balanced("((({[]}))") == False)

# Test case 10: Only opening brackets
print( is_balanced("({[") == False)

# Test case 11: Only closing brackets
print( is_balanced("}])") == False)