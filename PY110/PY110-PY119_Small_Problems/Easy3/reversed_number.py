#P
# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

# Input:
#     -
# Output:
#     -
# Explicit Rules:
#     -
# Implicit Rules:
#     -
# Question:
#     - 
#E
# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

#D


#A
def reverse_number(number):
    return int(str(number)[::-1])
#C

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True