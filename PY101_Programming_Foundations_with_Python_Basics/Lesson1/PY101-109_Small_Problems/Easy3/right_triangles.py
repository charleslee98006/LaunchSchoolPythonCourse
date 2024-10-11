def triangle(limit_integer):
    for i in range(1, limit_integer + 1):
        print(f'{' ' * (limit_integer - i)}{'*' * i}')

triangle(5)
triangle(9)