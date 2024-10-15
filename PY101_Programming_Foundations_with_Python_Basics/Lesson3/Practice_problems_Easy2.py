# Question 1:
# Way 1 -
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
reversed_number = numbers[::-1]
reversed_number2 = list(reversed(numbers))
# print(reversed_number)
# print(reversed_number2)

# Way 2 - 
# Question 2:
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# Question 3:
# print(42 in range(10, 101))
# print(100 in range(10, 101))
# print(101 in range(10, 101))

# Question 4:
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
# print(numbers)

# Question 5:
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
# print(type(numbers) == list)
# print(type(table) == list)

# Question 6:
title = "Flintstone Family Members"
centered_text = f"        {title}        "
# print(centered_text)
# centered_text2 = title.center(40)
# print(centered_text2)

# Question 7:
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
# print(statement1.count('t'))
# print(statement2.count('t'))

# Question 8:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
# print(ages.get('Spot'), 'Was unable to find it.')
# print('32' in ages)

# Question 9:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages['Marilyn'] = additional_ages['Marilyn']
ages['Spot'] = additional_ages['Spot']
print(ages)
