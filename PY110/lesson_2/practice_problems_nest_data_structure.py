# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
# # print(lst1[2][1][3])
# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]
# # print(lst2[1]['third'][0])

# lst3 = [['abc'], ['def'], {'third': ['ghi']}]
# # print(lst3[2]['third'][0][0])

# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
# # print(dict1['b'][1])
# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
# dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
# list1 = list(dict2['3rd'].keys())
# print(list1[0])

# a = 2
# b = [5, 8]
# lst = [a, b] # lst = [2, [5,8]]

# lst[0] += 2 # => list[0] = list[0] + 2 = list[0] = 2 + 2 => list = [4, [5,8]]
# lst[1][0] -= a #=> list[1][0] = list[1][0] - 2 => list[1][0] = 5 - 2 => list[4, [3,8]]

# a = 2
# b = [3, 8]

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# for name, info in munsters.items():
#     print(f'{name} is a {info['age']}-year-old {info['gender']}.')

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# running_total = 0
# for number, info in munsters.items():
#     if(info['gender'] =='male'):
#         running_total += info['age']

# print(running_total)

# total_age = sum([info['age'] for info in munsters.values() if(info['gender'] =='male')])
# print(total_age)
    
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# new_list = [sorted(inner_list) for inner_list in lst]
# print(new_list)

# def convert_to_string(element):
#     return str(element)

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# new_list = [sorted(inner_list, key=convert_to_string) for inner_list in lst]
# print(new_list)

# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]
# dictionary = {inner_list[0]: inner_list[1] for inner_list in lst }
# print(dictionary)

# def sum_odd_numbers(list1):
#     return sum([number for number in list1 if number % 2 == 1])
    
    
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# new_list = sorted(lst, key=sum_odd_numbers)
# print(new_list)

# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
# new_list = [{ key: value + 1 for dictionary in lst for key, value in dictionary.items() }]
# print(new_list)
    
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# master_list = []
# for inner_list in lst:
#     new_inner_list = []
#     for number in inner_list:
#         if number % 3 == 0:
#             new_inner_list.append(number)
#     master_list.append(new_inner_list)
# print(master_list)

# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# new_list = []

# for sublist in lst:
#     new_sublist = [num for num in sublist if num % 3 == 0]
#     new_list.append(new_sublist)

# print(new_list)

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
# new_list = [ value for item in dict1.values() for key, value in item.items() if (key =='colors' or key == 'size') ]
# for index_postion in range(0, len(new_list)):
#     if type(new_list[index_postion]) == str: 
#         new_list[index_postion] = new_list[index_postion].upper()
#     else if type(new_list[index_postion]) == list:
#         for 
# print(new_list)
# def transform_item(item):
#     if item['type'] == 'fruit':
#         return [color.capitalize() for color in item['colors']]
#     else:
#         return item['size'].upper()

# result = [transform_item(item) for item in dict1.values()]
# print(result)

# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]
# new_list = []
# for dictionary in lst 
#     for key, inner_list in dictionary.items():
#         is_all_even = True
#         if all(elements % 2 != 0 for elements in inner_list)
#             is_all_even = False
#         if(is_all_even):
#             new_list.append(dictionary)
# print(new_list)

# print(new_list)

# new_list = [dictionary for dictionary in lst for key,value in dictionary.items() ]
# print(new_list)
# def create_uuid():
#     alphabet_list = ['a','b','c','e','d','f']
#     [ for ]