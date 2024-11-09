# def select_fruit(dictionary):
#     new_dict = {}
#     # for key, value in dictionary.items():
#     #     if(value == 'Fruit'):
#     #         new_dict[key] = value
#     # return new_dict
#     return { key : value for key, value in dictionary.items() if value == 'Fruit' }


# produce = {
#     'apple': 'Fruit',
#     'carrot': 'Vegetable',
#     'pear': 'Fruit',
#     'broccoli': 'Vegetable',
# }

# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

# def double_numbers(numbers):
#     for index in range(0, len(numbers)):
#         numbers[index] *= 2
#     return numbers
#     # doubled_nums = []

#     # for current_num in numbers:
#     #     doubled_nums.append(current_num * 2)

#     # return doubled_nums

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
# print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

# def double_odd_index_position(numbers):
#     return [numbers[index] *2 if index % 2 == 1 else numbers[index] for index in range(0, len(numbers)) ]

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_odd_index_position(my_numbers))  # [1, 8, 3, 14, 2, 12]

# # not mutated
# print(my_numbers)                      # [1, 4, 3, 7, 2, 6]


def multiply(int_list, multiplying_number):
    return [ element * multiplying_number for element in int_list ]

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [1, 4, 3, 7, 2, 6]