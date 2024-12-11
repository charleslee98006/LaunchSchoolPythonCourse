#Problem
# Input:
#     - string text
# Output:
#     - dictionary
# Explicit Rules:
#     - dictionary keys are unique characters in the string 
#     - dictionary values are tuple of
#         - frequency of character in string
#         - percentage the string made up by the character
#     - dictionary should be sorted by descending order
#     - ties are broken by alphabetical
# Implicit Rules:
#     - cases are treated as separate values
# Question:
#     - 
#Examples

    # Test case 1: Basic functionality
    # assert frequency_analysis("hello world") == {
    #     'l': (3, 27.27),
    #     'o': (2, 18.18),
    #     ' ': (1, 9.09),
    #     'd': (1, 9.09),
    #     'e': (1, 9.09),
    #     'h': (1, 9.09),
    #     'r': (1, 9.09),
    #     'w': (1, 9.09)
    # }

    # # Test case 2: Empty string
    # assert frequency_analysis("") == {}

    # # Test case 3: Single character
    # assert frequency_analysis("a") == {'a': (1, 100.00)}

    # # Test case 4: All same characters
    # assert frequency_analysis("aaaa") == {'a': (4, 100.00)}

    # # Test case 5: Case sensitivity
    # assert frequency_analysis("aAaA") == {'a': (2, 50.00), 'A': (2, 50.00)}

    # # Test case 6: Special characters and numbers
    # assert frequency_analysis("a1b2c3!@#") == {
    #     'a': (1, 11.11),
    #     'b': (1, 11.11),
    #     'c': (1, 11.11),
    #     '1': (1, 11.11),
    #     '2': (1, 11.11),
    #     '3': (1, 11.11),
    #     '!': (1, 11.11),
    #     '@': (1, 11.11),
    #     '#': (1, 11.11)
    # }

    # # Test case 7: Longer string with varied frequencies
    # assert frequency_analysis("abracadabra") == {
    #     'a': (5, 45.45),
    #     'b': (2, 18.18),
    #     'r': (2, 18.18),
    #     'c': (1, 9.09),
    #     'd': (1, 9.09)
    # }
#Data Structures
# - sets to get the unique characters
# - dictionary as required by rule

#Algo
# def frequency_analysis(text):
#     1. get the unique values sets from the text
#     2. create and populate the dictionary with character as key and value as tuple of count and percentage up to 2 floating points
#     3. sort by count and by alphabet

    
#Code
def count(items):
    return -items[1][0], items[0]

def frequency_analysis(text):
    unique_char_set = set(text)
    new_dict = { character : (text.count(character), float("{:.2f}".format((text.count(character)) / len(text) * 100))) for character in unique_char_set}
    sorted_dict = dict(sorted(new_dict.items(), key=count))
    return sorted_dict

# Test case 1: Basic functionality
print(frequency_analysis("hello world") == {
    'l': (3, 27.27),
    'o': (2, 18.18),
    ' ': (1, 9.09),
    'd': (1, 9.09),
    'e': (1, 9.09),
    'h': (1, 9.09),
    'r': (1, 9.09),
    'w': (1, 9.09)
})

# Test case 2: Empty string
print(frequency_analysis("") == {})

# Test case 3: Single character
print(frequency_analysis("a") == {'a': (1, 100.00)})

# Test case 4: All same characters
print(frequency_analysis("aaaa") == {'a': (4, 100.00)})

# Test case 5: Case sensitivity
print(frequency_analysis("aAaA") == {'a': (2, 50.00), 'A': (2, 50.00)})

# Test case 6: Special characters and numbers
print(frequency_analysis("a1b2c3!@#") == {
        'a': (1, 11.11),
        'b': (1, 11.11),
        'c': (1, 11.11),
        '1': (1, 11.11),
        '2': (1, 11.11),
        '3': (1, 11.11),
        '!': (1, 11.11),
        '@': (1, 11.11),
        '#': (1, 11.11)
})

# Test case 7: Longer string with varied frequencies
print(frequency_analysis("abracadabra") == {
        'a': (5, 45.45),
        'b': (2, 18.18),
        'r': (2, 18.18),
        'c': (1, 9.09),
        'd': (1, 9.09)
})