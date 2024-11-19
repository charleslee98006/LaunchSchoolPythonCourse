def swap_ends(lst):
    first = lst[0]
    last = lst[-1]

    lst[0] = last
    lst[-1] = first
    return lst

new_list = [None,2,3,4,5,6,7]
print(swap_ends(new_list))