# Question 1:
numbers = [1, 2, 3, 4]
# numbers.clear()
numbers = []
# print(numbers)

# Question 2:
# list will combined and print [1,2,3,4,5]

# Question 3: Wrong; Will need to remember!
# Will print out the word "goodbye!" beause str2 and str1 is point to the same object
str1 = 1
str2 = str1
str2 = "goodbye!"
print(str1)
# The output is hello there. 
# In Python, strings are immutable so there is no way to 
# change the value of str1 unless we reassign it. 
# When we do str2 = str1 we are pointing the variable 
# str2 to the same memory location as the original string. 
# Once we reassign str2 again, on line 3, it just changes 
# what str2 variable points to, and doesn't affect variable str1.

# Remember that data types mutability vs immutability will/will not
# allow their values to change!


# Question 4:
#[{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)


# Question 5:
# def is_color_valid(color):
#     return color == "blue" or color == "green":
# def is_color_valid(color):
#     return (color is 'blue' or color is 'green')
# print(is_color_valid('blue'))
# print(is_color_valid('green'))
# print(is_color_valid('black'))