#P
# Write a function that takes a string as an argument and returns that string 
# with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 
# 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.
# Input:
#     - take in a string 
# Output:
#     - return a string
# Explicit Rules:
#     -every occurrence of word number convert to corresponding digital value
# Implicit Rules:
#     - mapping in order to correctly convert
# Question:
#     - 
#E
# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

#D
# -dictionary to map out the digital correspondent number


#A
def word_to_digit(text):
    word_number_digit_map = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
        'zero':'0',
    }
    converted_words_list = [ word_number_digit_map.get(word) if word_number_digit_map.get(word, '') else word for word in text.split()]
    print(converted_words_list)
    return ' '.join(converted_words_list)
        
#C


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True