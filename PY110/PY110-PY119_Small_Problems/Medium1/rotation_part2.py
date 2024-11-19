#P
# Write a function that rotates the last count digits of a number. 
# To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.
# Input:
#     - integer number and the digit position of the number
# Output:
#     - integer value from rotation
# Explicit Rules:
#     - based on the number position, move digit into the the end
# Implicit Rules:
#     -
# Question:
    # - 
#E
# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

#D
# - will need lists

#A
# def rotate_rightmost_digits(integer, position):
#     1. convert the integer into an string
#     2. create a variabble with and assign it with character based on the digit position
#     3. create a variable and assign the character via slices from the beginning to the digit position
#     4. create a variable and assign the character via sclieces from after digit position to the length of the string
#     5. combine all three variable such that step 3 in front of step 4, which is in front of step 2
#     6. convert the string to integer and return the new number

def rotate_rightmost_digits(integer, position):
    if(position !=1):
        string_version = str(integer)
        return int(string_version[:-position] + string_version[-position + 1 : ] + string_version[-position])
    return integer




print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
