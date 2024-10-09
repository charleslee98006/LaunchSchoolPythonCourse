def print_odd_numbers(max_integer):
    if isinstance(max_integer, int) and max_integer > 0:
        for number in (range(1, max_integer + 1, 2)):
            print(number)
    else:
        print('Please use integers greater than 0')

print_odd_numbers(99) # Prints 1 2 3 ... 99 in separate line
print_odd_numbers(1) # Prints 1 in separate line
print_odd_numbers(-1) # Prints 'Please use 0 or positive integers'
print_odd_numbers(2) # Prints 1 in separate line
print_odd_numbers(99.0) # Prints 'Please use 0 or positive integers'
print_odd_numbers('value') # Prints 'Please use 0 or positive integers'
print_odd_numbers(None) # Prints 'Please use 0 or positive integers'