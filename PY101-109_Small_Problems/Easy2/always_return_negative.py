def negative(number):
    if (isinstance(number, int)):
        return -number if number > 0 else number
    else:
        raise ValueError('Please use integers only.')

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True