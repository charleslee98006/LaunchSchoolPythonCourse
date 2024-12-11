# #Problem
# -Input
#     - string text
# -Output
#     - dictionary - keys are unique words in string and values are count the word appears in string
#     -
# -Explicit Rules
#     - Uppercase and lower case should be treated the same
#     -  ignoring punctuations
# -Implicit Rules
#     - Words are separated by spacing

# #Examples

# # # Test case 1: Simple sentence
# # print("Test case 1:")
# # result = word_frequency("The quick brown fox jumps over the lazy dog")
# # expected = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
# # print(f"Expected: {expected}")
# # print(f"Got: {result}")
# # print("Passed" if result == expected else "Failed")
# # print()

# # # Test case 2: Sentence with punctuation and mixed case
# # print("Test case 2:")
# # result = word_frequency("Hello, hello! How are you? Are you OK?")
# # expected = {'hello': 2, 'how': 1, 'are': 2, 'you': 2, 'ok': 1}
# # print(f"Expected: {expected}")
# # print(f"Got: {result}")
# # print("Passed" if result == expected else "Failed")
# # print()

# # # Test case 3: Empty string
# # print("Test case 3:")
# # result = word_frequency("")
# # expected = {}
# # print(f"Expected: {expected}")
# # print(f"Got: {result}")
# # print("Passed" if result == expected else "Failed")
# # print()

# #DS
# # - dictionary to hold the key value pairs
# #

# #Algo
# def word_frequency(text):
#     1. lower all casing and remove all punctuations from text
#     2. break all strings into string array and get a set from them
#     3. add the values from the set as keys into the dictionary and add the count to the corresponding key
#     4. return the dictionary

#Code
import string

def word_frequency(text):
    translator = str.maketrans('','', string.punctuation)
    no_punc_text = text.lower().translate(translator)
    result_dict = {word: no_punc_text.count(word) for word in set(no_punc_text.split())}
    print(no_punc_text)
    return result_dict


# Test case 1: Simple sentence
print("Test case 1:")
result = word_frequency("The quick brown fox jumps over the lazy dog")
expected = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
print(f"Expected: {expected}")
print(f"Got: {result}")
print("Passed" if result == expected else "Failed")
print()

# Test case 2: Sentence with punctuation and mixed case
print("Test case 2:")
result = word_frequency("Hello, hello! How are you? Are you OK?")
expected = {'hello': 2, 'how': 1, 'are': 2, 'you': 2, 'ok': 1}
print(f"Expected: {expected}")
print(f"Got: {result}")
print("Passed" if result == expected else "Failed")
print()

# Test case 3: Empty string
print("Test case 3:")
result = word_frequency("")
expected = {}
print(f"Expected: {expected}")
print(f"Got: {result}")
print("Passed" if result == expected else "Failed")
print()