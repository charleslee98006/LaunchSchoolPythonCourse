def rotate_rightmost_digits(integer, position):
    if(position !=1):
        string_version = str(integer)
        return int(string_version[:-position] + string_version[-position + 1 : ] + string_version[-position])
    return integer

def max_rotation(integer):
    for index in list(reversed(range(1, len(str(integer))+1))):
        integer = rotate_rightmost_digits(integer, index)
    return integer
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True