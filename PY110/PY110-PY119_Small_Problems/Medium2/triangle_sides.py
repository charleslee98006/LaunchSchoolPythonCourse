#P
# Input:
#     - 3 arguments (numbers)
# Output:
#     - return either 'equilateral', 'isosceles', 'scalene', or 'invalid'.
# Explicit Rules:
#     - definitions of a triangle:
#         - Equilateral: All three sides have the same length.
#         - Isosceles: Two sides have the same length, while the third is different.
#         - Scalene: All three sides have different lengths.
#     - the sum of the lengths of the two shortest sides must be greater than the length of the longest side
#     - every side must have a length greater than 0
# Implicit Rules:
#     -
# Question:
#     - 
#E
# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

#D
# we are going to use a list

#A
# def triangle(number1, number2, number3):
#     if all numbers equal to each other:
#         return equalateral
#     elif any two sides equal to each other but one isn't:
#         return isosceles
#     else:
#         return Scalene
#C
def triangle(number1, number2, number3):
    new_list = [number1, number2, number3]
    new_list_copy = [number1, number2, number3]
    max_number = max(new_list_copy)
    max_number_position = new_list_copy.index(max_number)
    new_list_copy.pop(max_number_position)
    sum_of_other_elements = sum(new_list_copy)
    
    if 0 in new_list or sum_of_other_elements < max_number:
        return 'invalid'
    elif new_list.count(number1) == 2 or new_list.count(number2) == 2 or new_list.count(number3) == 2:
        return 'isosceles'
    elif new_list.count(number1) == 3:
        return 'equilateral'
    else:
        return 'scalene'
    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True