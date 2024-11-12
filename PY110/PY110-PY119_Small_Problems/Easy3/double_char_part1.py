#P
# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.
# Input:
#     -
# Output:
#     -
# Explicit Rules:
#     -
# Implicit Rules:
#     -
# Question:
#     - 
#E
# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

#D


#A
def repeater(text):
    new_string = ''
    for char in text:
        new_string += char*2
    return new_string
#C

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True