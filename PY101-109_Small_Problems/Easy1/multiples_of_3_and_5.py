def multisum(max_number):
    if isinstance(max_number, int) or max_number > 0:
        list1 = list(range(3, max_number + 1, 3))
        list2 = list(range(5, max_number + 1, 5))
        return sum(set(list1 + list2))
    else:
        raise ValueError('Please use integers and values greater than zero for the argument.')

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)