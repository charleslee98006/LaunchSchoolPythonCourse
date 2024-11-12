#P
# input
#     - takes in a string of zero or more space-separated words
# output
#     - return a dictionary showing the number of different sized words
# Explcit Rules
#     - words consists of any sequence of non-space characters for the input
# Implicit Rules
#     - There will be multiple words with spaces separators
#     - Separate the words based on the spacing
# Questions
#     - Empty string?
#     - How to treat special characters?
#     - What does the resulting dictionary look like?
#     - What if we have two different words that have the same length?
#     - do we need to consider subset of words within the word ex. 'concatention' has 'cat' 
#E
# All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

# words within words are not part of the consideration; just need the entirety of word.
# dictionary is to return key of count and number of occurrences
# empty string will return empty dictionary
# punctation is considered part of the word count

#D
# we will need a dictionary since we need to return a dictionary as an output. We will need a
# list to separate each word from the initial string.

#A
# def word_sizes(text):
#     1. separate the words from the text argument based on the whitespace into a new list called new_list
#     2. create a empty dictionary called result_dict
#     3. iterate over the new_list and do the following:
#         1. check the dictionary to see if the word count key exists:
#             - if not, create a new word count key and assign key with the value of 1
#             - if yes, increment value and update the dictionary key
#     4. return result_dict
    
#C
# def word_sizes(text):
#     result_dict = {}
#     if(text):
#         for word in text.split(' '):
#             result_dict[len(word)] = result_dict.get(len(word), 0) + 1
#     return result_dict

# All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})