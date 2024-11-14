def sum_digits(number):
    exponent_number = 1
    new_list = []
    while number > 0:
        digit = number % 10**exponent_number // 10**(exponent_number-1)
        new_list.append(digit)
        number -= (digit * 10**(exponent_number-1))
        exponent_number +=  1
    return sum(new_list)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True