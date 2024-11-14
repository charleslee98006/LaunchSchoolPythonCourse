#P
# Input:
#     - array of words
# Output:
#     - return an array of position from string
# Explicit Rules:
#     - Input consists of alphabet characters; 
#         - uppercase and lowercase combo; 
#         - no space
#     - each characters has a mapping with integer position as the following:
#         - The letter `a` is in position 1
#         - `b` is in position 2. etc etc
# Implicit Rules:
#     - ranges are bounded from 1 to end of alphabet (abcdefghijklmnopqrstuvwxyz => 26)
# Question:
#     - empty string?
#     - The capitalized version of the character as the lower case version?
#E
# console.log(solve(["abode","ABc","xyzD"])); // [4,3,1]
# console.log(solve(["abide","ABc","xyz"]));  // [4,3,0]
# console.log(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"])); // [6,5,7]
# console.log(solve(["encode","abc","xyzD","ABmD"])); // [1, 3, 1, 3]

#D
# - Variable constant assigned with string array

#A
# def solve(list1):
#     1. create a empty list called count_list
#     2. create a variable called counter and give it zero
#     3. create a constant of the alphabet characters from a to z
#     4. go through the each letters of each word and 
#     5. Check each letters matches with the character in the alphabeteic characters string based on the index position regardless of casing
#         - if matches, increment the counter tally by 1
#         - When loop ends, add the tally to the count_list and reset the counter tally to zero 
#     6. return the count_list

#C
def solve(list1):
    count_list = []
    alphabet_characters = 'abcdefghijklmnopqrstuvwxyz'
    for word in list1:
        counter = 0
        for index in range(0, len(word)):
            if(word[index].lower() == alphabet_characters[index]):
                counter += 1
        count_list.append(counter)
    return count_list

# print(solve(["abode","ABc","xyzD"])); # [4,3,1]
# print(solve(["abide","ABc","xyz"]));  # [4,3,0]
# print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"])); # [6,5,7]
# print(solve(["encode","abc","xyzD","ABmD"])); # [1, 3, 1, 3]