def print_even_numbers(max_integer):
    if isinstance(max_integer, int) and max_integer > 1:
        for number in (range(2, max_integer + 1, 2)):
            print(number)
    else:
        print('Please use integers greater than 1')

print_even_numbers(99) # Prints 1 2 3 ... 99 in separate line
print_even_numbers(2) # Prints 2 in separate line
print_even_numbers(1) # Prints 'Please use integers greater than 1'
print_even_numbers(-1) # Prints 'Please use integers greater than 1'
print_even_numbers(99.0) # Prints 'Please use integers greater than 1'
print_even_numbers('value') # Prints 'Please use integers greater than 1'
print_even_numbers(None) # Prints 'Please use integers greater than 1'