#P
# Input:
#     - the length of the desired fib number
# Output:
#     - the index of the first Fibonacci number that has the number of digits by the input
# Explicit Rules:
#     - 
# Implicit Rules:
#     - will have to be creater greater
# Question:
#     - 
#E
# # All of these examples should print True
# # The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)

#D
# - list to contains all of the fib numbers


#A
# def something(parameter):
#     1.
#C


import sys

sys.set_int_max_str_digits(50_000)

memo = {}
def fibonacci(nth):
    if nth <= 2:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]
    
def find_fibonacci_index_by_length(number):
    count = 1
    found_len = False
    while not found_len:
        fib_number = fibonacci(count)
        new_list = [1,1] + list(memo.values())
        if(len(str(new_list[-1])) == number):
            return len(new_list)
        count +=1
    

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)