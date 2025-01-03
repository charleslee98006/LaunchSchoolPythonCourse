#1. Write a program that asks the user for two numbers and divides the first number by the second number. 
# Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).
# try:
#     input1 = int(input('Please select a number: '))
#     input2 = int(input('Please select another number: '))
#     print(f'Result is: { input1 / input2}')
# except ValueError:
#     print('Please enter valid numbers!')
# except ZeroDivisionError:
#     print('Cannot divide by zero!')
    
#2. Expand your answer to the previous program so it prints the result only when no exceptions are raised. 
# You should also print End of the program regardless of whether an exception is raised.

# try:
#     input1 = int(input('Please select a number: '))
#     input2 = int(input('Please select another number: '))
#     result = input1 / input2
# except ValueError:
#     print('Please enter valid numbers!')
# except ZeroDivisionError:
#     print('Cannot divide by zero!')
# else:
#     print(f'Result is: { result }')
# finally:
#     print('End of the program')

#3. Modify your answer to the previous problem so it handles both ZeroDivisionError and ValueError with a single exception handler. 
# The output for both exception types can be obtained from the exception object.
# try:
#     input1 = int(input('Please select a number: '))
#     input2 = int(input('Please select another number: '))
#     result = input1 / input2
# except (ZeroDivisionError, ValueError) as e:
#     print(f'Error: {e}')
# else:
#     print(f'Result is: { result }')
# finally:
#     print('End of the program')
    
# 4. Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. 
# If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.

# input1 = int(input('please select a number: '))
# if input1 < 0:
#     raise ValueError('Please select a zero or positive number.')
# print(f'Value is: {input1}')

#5. Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.

# class NegativeNumberError(Exception):
#     def __init__(self, message='Please select a zero or positive number.'):
#         super().__init__(message)
    
# input1 = int(input('please select a number: '))
# if input1 < 0:
#     raise NegativeNumberError()
# print(f'Value is: {input1}')

# class NegativeNumberError(ValueError): # The reason this works because you are inheriting ValueError and are passing the statement implicitly.
#     pass

# num = float(input('Enter a number: '))
# if num < 0:
#     raise NegativeNumberError('Negative numbers are not allowed!')
# print(f'You entered {num}')

# 6. Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.
# def inverse(list1):
#     try:
#         return [1 / float(number) for number in list1]
#     except ValueError:
#         print('number should not be a string')
#     except OverflowError:
#         print('Please select a number from 0 to 100')
#     except ZeroDivisionError:
#         print('number cannot be divided by zero!')

# a = [1,0]
# print(inverse(a)) # ZeroDivisionError exception 
# a = ['joe',1, 0.2]
# print(inverse(a)) # ValueError exception 
# b = [3**1000, 0.2]
# print(inverse(b)) # handled values over max int value
# a = [1,2,3,4,5,6]
# print(inverse(a)) # works

# 7. Which of the following code snippets would raise a ZeroDivisionError?
# a) 5 / 2
# b) 3 // 0
# c) 8 % (1 - 1)
# d) 7 / (3 + 4)

#Answer: b and c  

#8. Given the following gloval dictionary:
# students = {'John': 25, 'Jane': 22, 'Doe': 30}
# # Write a Python function get_age(name) that takes a student's name as an argument and returns their age. 
# # If the student's name isn't in the dictionary, the function should return 'Student not found'.

# def get_age(name):
#     try:
#         return students[name]
#     except KeyError:
#         return 'Student not found'

# print(get_age('John'))
# print(get_age('john'))
# print(get_age(0))

#9. Given the following list:
numbers = [1, 2, 3, 4, 5]
# Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. 
# In both cases, the function should return None when the element isn't found.

#LBYL Approach:
def fetch_element_lybl(position):
    if not isinstance(position, int):
        return 'Please use integer values only'
    elif position > len(numbers):
        return None
    else:
        return numbers[position]

#AFNP approach:
def fetch_element_afnp(position):
    try:
        return numbers[position]
    except IndexError:
        return None
    except TypeError:
        raise
    
print(fetch_element_lybl(6))
print(fetch_element_afnp(6))

#10. Which of the following code snippets would raise an AttributeError?
# a) 'hello'.upper()
# b) [1, 2, 3].push(4) - this one
# c) {'key': 'value'}.get('key')
# d) (12345).length() - This one

#Answer:b and d