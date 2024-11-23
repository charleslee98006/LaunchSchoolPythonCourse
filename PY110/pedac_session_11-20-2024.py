#Problem
# Count the number of 'pair letters' in a given string.
# A pair letter is when two of the same letter appear in sequence.
# Pairs cannot overlap.

# -input
#     - string text
# -Output
#     - return integer
# -Explicit Rules
#     - Tally the number of lettered pairs from the text
#     - A lettered pair is when two letters are next to each other
#     - if one pair and another pair uses the same letters, they do not count
# -Implicit Rules
#     - To have a overlap characters, you need 3+ of the same characters
# -Questions


#Examples:
# Tests
# print(count_duplicates('success'))  # 2
# print(count_duplicates('aabbccc'))  # 3
# print(count_duplicates('aabbcccc')) # 4

#Data Structures
# - dictionary

#Algo
# def count_duplicates(word):
    # 1. Create an initial `running_total`= zero
    # 2. Create a variable called `overlap_index` = -1
    # 3. iterate over the word by index:
    #     1. compare the character in index and character in index + 1 and over `overlap_index` != index:
    #         1. increment the running_total
    #         2 set overlap_index = index+1
    # 4. return the running_total
#Code


def count_duplicates(word):
    running_total = 0
    overlap_index = -1
    for index in range(len(word)-1):
        character = word[index]
        character2 = word[index + 1]
        if character == character2 and overlap_index != index:
            running_total += 1
            overlap_index = index + 1
    return running_total

# Tests
print(count_duplicates('aaa'))      # 1
print(count_duplicates('aaaa'))     # 2
print(count_duplicates('aaaab'))    # 2
print(count_duplicates('success'))  # 2
print(count_duplicates('aabbccc'))  # 3
print(count_duplicates('aabbcccc')) # 4
print(count_duplicates('aaaaaaabbcccc')) # 6
