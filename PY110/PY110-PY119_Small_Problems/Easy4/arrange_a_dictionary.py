def sort_by_values(item):
    key, value = item
    return value

def order_by_value(dictionary):
    new_list = sorted(dictionary.items(), key=sort_by_values)
    new_keys_list = [pair[0] for pair in new_list]
    return new_keys_list

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']

print(order_by_value(my_dict) == keys)  # True