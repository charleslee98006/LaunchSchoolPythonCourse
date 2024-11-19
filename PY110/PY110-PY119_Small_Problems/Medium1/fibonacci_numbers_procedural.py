#P
# Input:
#     - nth fib number
# Output:
#     - result the nth fib number
# Explicit Rules:
#     - a sequence of numbers in which each number is the sum of the previous two numbers
# Implicit Rules:
#     - Fib numbers required two values before increasing
# Question:
#     - 
#E
# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True

#D
# - will need a list to keep track of every number

#A
# def fibonacci(nth_number):
#     1. if nth_number is less than 2 return 1
#     2. else
#         1. Create a list with first and second element have the 1 integer value
#         2. in a loop with the range that starts from 2 and ends to the nth number:
#             1. add the previous two elements
#             2. add the sum to the list
#         return the sum of last two elements from the list 
#C
def fibonacci(nth_number):
    if(nth_number <= 2):
        return 1
    new_list = [1,1]
    for index in range(2, nth_number):
        new_list.append(new_list[index-2] + new_list[index - 1])
    return new_list[-1]


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True