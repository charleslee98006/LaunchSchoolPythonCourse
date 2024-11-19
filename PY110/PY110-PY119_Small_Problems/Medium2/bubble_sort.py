# Problem
# Input
# - list
# Output
# - same list but augmented 
# Explicit Rules
# -
# Implicit Rules
# -
# Questions
# - 
#Example

# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True

#Algorithm



#Code
def swap(position1, position2, original_list):
    temp = original_list[position1]
    original_list[position1] = original_list[position2]
    original_list[position2] = temp


def bubble_sort(list1):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for index in range(len(list1)-1):         
            element1 = list1[index]
            element2 = list1[index + 1]
            # print(element1)
            # print(element2)
            if element1 > element2:
                has_swapped = True
                swap(index, index + 1, list1) 
            # print(list1)
    return list1

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True