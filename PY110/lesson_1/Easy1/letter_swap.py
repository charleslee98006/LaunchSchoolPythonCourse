#P
# Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. 
# You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.
#
# input
#     -String of words separated by space
# output
#     -return a string
# explicit rules
#     - swap the first and last letters of every word
#     - string has at least 1 word
#     - every word contains one letter
#     - contains nothing but words and spaces
#     - no leading, trailing or repeated spaces
# implicit rules
#     - can expect no non-words
# question
#     - Not really.
    
#E
# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

#D
# will need a list since we to split the words and get each word
#A
# def swap(text):
#     1. split the text into a list of words
#     2. iterate through the list of words and do the following:
#         1. get the first letter and the last letter of the word
#         2. get the body of the word excluding the first and last letter
#         3. Combine the last letter first + body + first letter
#         3, assign the list at that position the newly combined word
#     3. with the list create a string from all of the words with space in between each word
#     return the string

#C
def swap(text):
    flipped_word_list = [ word[-1] + word[1 : len(word)-1] + word[0] if (len(word) > 1) else word for word in text.split() ]
    swapped_word = ' '.join(flipped_word_list)
    return swapped_word
    
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True