from fractions import Fraction

# Problem
# -Input
# -Output
# Explicit Rules

def egyptian(rational_number):
    fraction_version = Fraction(rational_number)
    initial_value = 1
    new_list_denom = []
    while fraction_version > 0:
        if fraction_version >= Fraction(1, initial_value):
            fraction_version -= Fraction(1, initial_value)
            new_list_denom.append(initial_value)
        initial_value +=1
    return new_list_denom


def unegyptian(list1):
    initial_value = 0
    for each in list1:
        initial_value += Fraction(1, each)
    return initial_value

# print(Fraction(1, 2) - Fraction(1, 2))
# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# # Using the unegyptian function
# # All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))