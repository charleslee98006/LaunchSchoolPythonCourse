import math

#Problem
# Input:
#     - list of integer
# Output:
#     - minimum int that can be appended to list > current sum of numbers ex. sum([1,2,3]) = 6
# Explicit Rules:
#     - list always have 2 ints
#     - numbers will be > 0
#     - duplicates can occur
# Implicit Rules:
#     - the smaller the resulting int the better
#     - appending must be done hence, we are to be adding 
# Question:
#     - 
#Examples
# print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
# print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
# print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
# print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37
# print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4) # Nearest prime to 163 is 167

#Data Structures
# -list of prime numbers

# #Algo
# def nearest_prime_sum(parameter):
#     1. get the sum of the list as the starting point
#     2. keep on incrementing until hit prime number
#     3. return the closest one distance from prime
    
#Code
def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def nearest_prime_sum(sum_list):
    initial_value = sum(sum_list) + 1
    if(initial_value == 2):
        return 1
    while True:
        check_prime_number = is_prime(initial_value)
        if(check_prime_number):
            break
        else:
            initial_value += 1
    print(initial_value)
    return initial_value- sum(sum_list)

print(nearest_prime_sum([1,1]) == 1)
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37
# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)