#Problem
# Input:
#     - single integer
# Output:
#     - reutn the sum of all multiple of 7 and 11 less than arg
# Explicit Rules:
#     -if number is mutiple of 11 and 7  - count once
#     - if arg is < 0, return 0
# Implicit Rules:
#     -
# Question:
#     - 
# #Examples

# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)

#Data Structures
# - list for all multiples of 11 and 7
# - set to get number once

# #Algo
# def something(parameter):
#     1. get a list of multiples of 7 that are less than the arg
#     2. get list of multiples of 11 that are less than the arg
#     3. combine the list together and remove duplicates with set
#     4. get the sum from list in step 3
#     5. return the sum
    
#Code
def seven_eleven(limit):
    seven_list = [number * 7 for number in range(limit) if (number*7 < limit)]
    eleven_list = [number * 11 for number in range(limit) if (number*11 < limit)]
    # print(seven_list)
    # print(eleven_list)
    combined_list = list(set(eleven_list + seven_list))
    # print(combined_list)
    return sum(combined_list)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)