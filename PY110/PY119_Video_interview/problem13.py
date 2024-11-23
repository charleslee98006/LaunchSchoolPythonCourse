# #Problem
# Input:
#     - two string arguments 
# Output:
#     - boolean
# Explicit Rules:
#     - return true if string arg1 can be rearrange to = arg2
#     - assumed lowercase only
# Implicit Rules:
#     -
# Question:
#     - 
# #Examples

# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)

# #Data Structures
# -dictionary to check sort all occurrence of letters for

# #Algo
# def unscramble(parameter):
    # 1. from the first arg check each character from the first character to the second string arguement
    #     1. If found remove the character
    #     2. if not found, return False
    # 2. return True if all characters in second string are in first string
    
#Code
def unscramble(text1, text2):
    original_length = len(text1)
    counter = 0
    while counter < len(text2):
        text1 = text1.replace(text2[counter], '', 1)
        if(len(text1) != original_length-counter-1):
            return False
        counter += 1
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)