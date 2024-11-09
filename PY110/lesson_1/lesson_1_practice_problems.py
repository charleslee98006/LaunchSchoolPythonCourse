#Practice Problem 1

# fruits = ("apple", "banana", "cherry", "date", "banana")
##How would you count the number of occurrences of "banana" in the tuple?
# print(fruits.count("banana"))

#Practice Problem 2

# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers)) # 7; wrong - should be 5 because it removes all dups
# #What is the set's length? Try to answer without running the code.

#Practice Problem 3

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# How would you obtain a set that contains all the unique values from both sets?
# print(a | b)

#Practice Problem 4
# Given the following code, what would the output be? Try to answer without running the code.
# names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
# name_positions = {}
# for index, name in enumerate(names):
#     name_positions[name] = index
# print(name_positions) # {Fred: 0, Barney: 1, Wilma: 2, Betty: 3, Pebbles: 4, Bambam: 5}


#Practice Problem 5
#Calculate the total age given the following dictionary:
# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }
#Solution 1
# total_age = 0
# for age in ages.values():
#     total_age += age # 6174

#Solution 2
# sum(ages.values()) # 6174

#Practice Problem 6
#Determine the minimum age from the above ages dictionary.
# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }
# print(min(ages.values())) # 10

#Practice Problem 7
# What would the following code output? Try to answer without running the code.
# words = ['ant', 'bear', 'cat']
# selected_words = []
# for word in words:
#     if len(word) > 3:
#         selected_words.append(word)
# print(selected_words) # ['bear']

#Practice Problem 8
#Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive:
# statement = "The Flintstones Rock".replace(' ', '')
# new_dict = {}
# for char in statement:
#     count = new_dict.get(char, 0)
#     new_dict[char] = count + 1        
# print(new_dict)

#Practice Problem 9
#What is the return value of the list comprehension below? Try to answer without running the code.
#[num for num in [1, 2, 3] if num > 1]
# Returns a list of numbers where the is greater than 1; hence, answer is [2,3]

#Practice Problem 10
# What does the following code print and why?
# dictionary = {'a': 'ant', 'b': 'bear'}
# print(dictionary.popitem())

# code will take from the dictionary variable and print the last key value pair, which is {'b': 'bear'}
# remember that popitem() will return a tuple instead and that dictionaries are "ordered" based on creation order sincePython 3.7+

#Practice Problem 11
# What does the following code return? Try to answer without running the code.
# lst = [1, 2, 3, 4, 5]
# lst[:2] # lst will return all elements up to index position 2 - not inclusive; hence, [1,2]
# print(lst[:2])

#Practice Problem 12
# What would be the output of the below code? Try to answer without running the code.
# frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6) # think it would throw an error because frozen sets are immutable, hence, you cannot add to it. Plus, add function does not exist for frozensets
# print(frozen)