# Question 1:
# for number in range(1,11):
#     print(f'{'-' * number}The Flintstones Rock!')

# Question 2:
# def factors(number):
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         if divisor > 0:        
#             divisor -= 1
#         else:
#             divisor += 1
#     return result
# print(factors(10))
# print(factors(-10))

# Question 3: - A bit off
# The key difference is that the buffer in buffer1 implementation
# is adding an element to the buffer in the first implementation, while 
# the second one is putting the new_element into a list and 
# then combine two list into 1 for the second implementation.

# Better answer: Yes, there is a difference. The first function (add_to_rolling_buffer1) mutates the original list represented by buffer. 
# The second function (add_to_rolling_buffer2) does not mutate the original list, but instead creates a new list and assigns it to buffer,
# whose value ultimately gets returned by the function.

# Question 4: WAs totally wrong on this
# print(0.3 + 0.6) # prints 0.9
# print(0.3 + 0.6 == 0.9) # prints boolean True
#If you thought that the outputs would be 0.9 and True, respectively, you were wrong. 
# Python uses floating point numbers for all numeric operations. Most floating point 
# representations used on computers lack a certain amount of precision, and that can yield unexpected results like these.
# Answers:
# 0.8999999999999999
# False

# Question 5: wrong
import math
nan_value = float("nan")
# print(nan_value)
# print(float("nan"))
# print(type(nan_value))
# print(type(float("nan")))
# print(math.isnan(nan_value)) #True

#Answer is False; Python doesn't let you use == to determine whether a value is nan.

# Question 6:
# What is the output of the following code?
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

# print(answer - 8) # My answer 34

# Question 7:
# Yes, the data has been ransacked because spot is accessing the inner dictionary value that and replacing the mutable values

# Question 8:
#print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
#print(rps(rps("paper","rock"), "rock"))
#print('paper') My answer is Paper

# Question 9:
# bar(foo()) -  foo returns "yes" no matter what.
# bar("yes") - ("yes" == "no") and ("yes" or "no") My Answer: False
# def foo(param="no"):
#     return param

# def bar(param="no"):
#     # print(foo() or "no")
#     # print((param == "no"))
#     # return (param == "no") and (foo() or "no")
#     return True and "no"

# print(True and "no")

# print(bar("no"))

# Question 10: wrong!
def foo():
    return 7777
a = 42
b = foo()
c = a
print(id(a))
print(id(b))
print(id(c))
print(id(a) == id(b) == id(c)) # My answer is false

# In Python, there's a predefined range of integers, specifically from -5 to 256, 
# for which memory locations are pre-assigned. When you reference an integer 
# within this span, Python consistently points to the same memory spot. 
# This strategy enhances efficiency since these particular numbers are commonly utilized in many programming scenarios.

#However, when you work with integers outside of this specific range, 
# Python doesn't assure that it will consistently point to the same memory address for identical values across different variables.