#P
# Input
#     - list of numbers
# Output
#     - list of numbers
# Explicit Rules
#     - same number of elements for input and output
#     - each element value being the running total from the original list
# Implicit Rules
#     - None that I can see.
# Question:
#     - Number being only integer? What about empty list
#E
# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# empty list  will return list; seems like integers only. 

#D
# List seems like the most natural option since we have to return them

#A
# def running_total(int_array):
#     1. Create a variable called running_total and assigned zero to it as the initial value
#     2. Create an empty list and assign it to the running_total_list variable
#     2. iteration through the int_array and do the following:
#         1. take the first element from the int_array and add to the running_total variable
#         2. add the running_total to the running_total_list variable 
#         3. stop only when reaching to the end of the int_array list 
#     3. return the running_total_list
#C
def running_total(int_array):
    print(int_array) # initial state of the list
    running_total = 0
    for index in range(0, len(int_array)):
        running_total += int_array[index]
        int_array[index] = running_total
    print(int_array)  # final state of the list from in place insertion
    return int_array
    
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True