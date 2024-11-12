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
def sequence(max_range):
    return list(range(1, max_range + 1))
#C

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True