def floating_point_arithmetics():
    first_number = input('==> Enter the first number:\n')
    second_number = input('==> Enter the second number:\n')
    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        raise ValueError('You need to use a number!')
    print(f'==> {first_number} + {second_number} = {first_number + second_number}')
    print(f'==> {first_number} - {second_number} = {first_number - second_number}')
    print(f'==> {first_number} * {second_number} = {first_number * second_number}')
    print(f'==> {first_number} / {second_number} = {first_number / second_number}')
    print(f'==> {first_number} // {second_number} = {first_number // second_number}')
    print(f'==> {first_number} % {second_number} = {first_number % second_number}')
    print(f'==> {first_number} ** {second_number} = {first_number ** second_number}')
    
floating_point_arithmetics()