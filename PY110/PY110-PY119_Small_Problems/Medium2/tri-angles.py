#Problem
# - Input
#     - 3 integer values
# - Output
#     - string word of 'right', 'acute', 'obtuse', or 'invalid'.
# - Explicit Rules
#     - Right: One angle is a right angle (exactly 90 degrees).
#     - Acute: All three angles are less than 90 degrees.
#     - Obtuse: One angle is greater than 90 degrees.
#     - the sum of the angles must be exactly 180 degrees
#     - every angle must be greater than 0
# - Implement Rules
# - Questions
#Example
# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True

#Data Structure
# - could use list methods by adding the values into a list
#Algorithm

#Code
def triangle(angle1, angle2, angle3):
    new_list = [angle1, angle2, angle3]
    if(0 in new_list) or sum(new_list) < 180:
        return 'invalid'
    elif 90 in new_list:
        return 'right'
    elif all(element < 90 for element in new_list):
        return 'acute'
    else:
        return 'obtuse'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True