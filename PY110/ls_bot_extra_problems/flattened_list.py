def flatten_list(nested_list):
    return recursion_list(nested_list, [])

def recursion_list(lst, resulting_list):
    # print(resulting_list)
    # print('lst: ', lst)
    for each in lst:
        if type(each) == int:
            resulting_list.append(each)
            # print('resulting_list: ', resulting_list)
        else:
            recursion_list(each, resulting_list)
    return resulting_list
# Test cases
print(flatten_list([1, [2, 3, [4, 5]], 6, [7, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8])
print(flatten_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
print(flatten_list([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5])
print(flatten_list([]) == [])