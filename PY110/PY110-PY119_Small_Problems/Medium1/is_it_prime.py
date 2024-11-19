#P
# Input:
#     - positive integer
# Output:
#     - boolean value:
#         - True if integer is prime
#         - False if not prime
# Explicit Rules:
#     - A prime number is a positive number that is evenly divisible only by itself and 1
#      - 1 is not a prime number
# Implicit Rules:
#     - numbers from 1 to 3 will always be prime
# Question:
#     - None; need to see examples
#E
# print(is_prime(1) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True

#D
# - Probably just need a to keep a running total

#A
# def is_prime(number):
#     1. in a for loop with the range from 1 to the positive integer number, do the following:
#         1. check to see if the number divided by the range element will equal to 0 raminders and not equal to 1, 2, 3
#             if yes, return False
#     2. return True once the for loop ends
#C

def is_prime(number):
    if(number == 1 ):
        return False
    for each in range(2, number):
        if(number % each == 0):
            return False
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True