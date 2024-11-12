#Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

# P
#     # input - asks user 6 numbers
#     # output - prints message where sixth number appears amongst the first five
#     # Explicit Rules
#         - take in 6 numbers
#         - print message if sixth number is in first five
#     # Implicit Rules
#         - input values will be in the form of strings
#         - sixth number is last number to use to check the first five,
#     # Question
#         - Numbers only?
#         - will numbers be given on the same input prompt?
#         - How should the message be printed out?
# E
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.
# Integers only. Seen how the message will be printed out

# D
# seems a list to do the boolean check `in`` operator. Let's keep this simple.

# A
# 1. Ask the users for 6 numbers
# 2. Check against the other 5 values with the sixth number
# 3. print out a message whether the sixth number is within the first five.

# C
def is_sixth_number_with_five():
    value1 = input('Enter the 1st number: ')
    value2 = input('Enter the 2nd number: ')
    value3 = input('Enter the 3rd number: ')
    value4 = input('Enter the 4th number: ')
    value5 = input('Enter the 5th number: ')
    value6 = input('Enter the last number: ')
    is_or_not = "isn't"
    if (value6 in [value1, value2, value3, value4, value5]):
        is_or_not = 'is'
    print(f'{value6} {is_or_not} in {value1},{value2},{value3},{value4},{value5}.')

is_sixth_number_with_five()