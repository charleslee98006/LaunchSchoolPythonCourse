def is_it_odd(number):
    return bool(abs(number) % 2) if isinstance(number, int) else 'Please use integers'
        
print(is_it_odd(0)) # Print False
print(is_it_odd(1)) # Print True
print(is_it_odd(-1)) # Print True
print(is_it_odd(2)) # Print False
print(is_it_odd(-2)) # Print False
print(is_it_odd(2.0)) # Print 'Please use integers' due to account for parameter restrictions
print(is_it_odd('Invalid String')) # Print 'Please use integers' due to account for parameter restrictions
print(is_it_odd(None)) # Print 'Please use integers' due to account for parameter restrictions