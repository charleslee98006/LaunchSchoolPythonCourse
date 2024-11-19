def sum_square_difference(number):
    sum_squared = sum(list(range(1, number +1))) **2
    squared_sum = sum([value**2 for value in range(1, number +1)])
    return sum_squared - squared_sum
    
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True