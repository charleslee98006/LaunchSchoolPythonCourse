def binary_search(list1, value):
    copy_list = list1.copy()
    starting_point = 0
    ending_point = len(copy_list)-1
    while starting_point <= ending_point:
        mid_point = (starting_point + ending_point) //2
        element = copy_list[mid_point]
        if(element == value):
            return mid_point
        elif value > element:
            starting_point = mid_point + 1
        else:
            ending_point = mid_point - 1
    return -1


# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)