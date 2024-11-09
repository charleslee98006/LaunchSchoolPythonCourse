## Step 1: Understand the Problem
# Sort Strings by Most Adjacent Consonants
# Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. 
# If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. 
# Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

# Tasks
# You are provided with the problem description above. Your tasks for this step are:

# Make notes of your mental model for the problem, including:
# inputs and outputs.
# explicit and implicit rules.
# Write a list of clarifying questions for anything that isn't clear.

# inputs - a list of strings
# output - sorted list by highest number of adjacent consonant a string contains

# # explicit rules:
#     - if two strings contains the same highest adjacent, original order are retained
#     - Consonants are considered adjacent:
#         - next to each other in the same word
#         - if is a space between the two consonant characters
# # implicit rules:
#     - list are is to be sorted from highest to lowest consonant adjacent characters
#     - we will need to keep a list of vowel to find consonant characters. 

# # Questions:
#     - What happens to single or empty lists? 
#     - how to deal with single character or combo of 1 vowel and consonant character?
#     - How are non-consonant strings are to be treated?
#     - How are we to treat special characters?

# Step 2: Examples and test cases
# You are provided with the following test cases for this problem.

# my_list = ['aa', 'baa', 'ccaa', 'dddaa'] -> [0, 0, 1, 3]
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan'] -> [ 1, 0 , 1, 4]
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar'] -> [0,0,0,0]
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year'] -> [0,0,3,0]
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb'] -> [3,4,4]
# print(sort_by_consonant_count(my_list))
## ['xxxx', 'xxxb', 'xxxa']

# Regarding your initial mental model and questions from Step 1, make some notes about the test cases. 
# Do the test cases confirm or refute different elements of your original analysis and mental model? 
# Do they answer any of the questions that you had, or do they perhaps raise further questions?

#Answer: confirm some, but does not handle empty strings. 

# Step 3: Data Structures
# list from the looks of it.

# Step 4: Algorithm 
# sort_by_consonant_count function (array_of_words):
# 1. Create a list of vowels
# 2. Go through each word in list and do the following:
#     1. tally how many adjacent consonants are there in the word(s) against the list of vowels
#     2. Track the tally with association to the word in a new list. They should be in order
# 3.  sort the new list with the highest adjacent consonant being first to the lowest.
#     - if adjacent constant the two are the same, move onto the next set
# 4. take all the words and place them into another new list call C
# 5. return the C list

# Step 5: Implement a Solution in Code
def sort_by_consonant_count(array_of_words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    dictionary = {}
    for text in array_of_words:
        count = 0
        i = 0
        j = 1
        while(j < len(text)):
            if(text[i] not in vowels and text[j] not in vowels):
                count +=1
            i += 1
            j += 1
        dictionary[text] = count
    result = []
    while len(dictionary) > 0:
        max_key = max(dictionary, key=dictionary.get)
        result.append(max_key)
        dictionary.pop(max_key, 'No Key found')
    return result
        
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar'] 
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year'] 
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']