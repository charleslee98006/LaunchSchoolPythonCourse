#Problem
# Input:
#     - string argument of all digits
# Output:
#     - the greatest product of 4 consecutive digits in the string
# Explicit Rules:
#     - string digit will always be greater than 4 digits
# Implicit Rules:
#     - order does matter, do not sort
#     - single numbers are to be discounted
# Question:
#     - 
#Examples

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

#Data Structures
# list - combinations that has 4 digits or more

#Algo
# def something(parameter):
    #  1. get all combinations of with len of 4
    #  2. convert string into digits and get multiple of the digits
    #  3. get the largest and return it
    
#Code
def greatest_product(digit_text):
    new_list = [digit_text[index: index2+1] for index in range(len(digit_text)) for index2 in range(index, len(digit_text)) if len(digit_text[index: index2+1]) == 4]
    converted_list  = []
    for substring in new_list:
        running_total = 1
        for digit in substring:
            running_total *= int(digit)
        converted_list.append(running_total)
    print(converted_list)
    return max(converted_list)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

