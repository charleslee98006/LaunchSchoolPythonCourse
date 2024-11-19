#P
# -Input
#     - String
# -Output
#     -Dictionary
# -Explicit Rules
#     - the percentage of characters in the string that are lowercase letters
#     - the percentage of characters that are uppercase letters
#     - the percentage of characters that are neither
#     - strings whose numeric values lie between "0.00" and "100.00"
#     - Each value should be rounded to two decimal points.
# - Inplicit Rules

# - Questions

# Examples
# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

#Data structure
# - running total; no list and Data structures for now

# Algorithm
# 1. Create 2 variables called Uppercase_count and Lowercase_count and set them to zero
# 2. In a loop, go through each character in the text and do the following:
#     1. check to see is character is a number:
#         if yes, check 
#             if is uppercase
#                 increment Uppercase_count by 1
#             else
#                 increment Lowercase_count by 1
# 5. subtract the string length by Uppercase_count and Lowercase_count to get the "neither" count
# 4. print the percentages up to 2 decimals places

# Code:
def letter_percentages(text):
    uppercase_count = 0
    lowercase_count = 0
    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1
    new_dict = {
        'lowercase': f'{lowercase_count / len(text)*100:.2f}',
        'uppercase': f'{uppercase_count / len(text)*100:.2f}',
        'neither': f'{(len(text) - uppercase_count - lowercase_count) / len(text)*100:.2f}',
    }
    return new_dict    
    
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)