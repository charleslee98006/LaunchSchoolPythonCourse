#P
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


#D


#A
def average(list1):
    average = 0
    for number in list1:
        average += number
    return average // len(list1)
#C

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True