def square(number):
    if number == None:
        raise ValueError('You gave a None type value.')
    elif isinstance(number, str):
        return float(number) * float(number)
    elif isinstance(number, list):
        return [value * value for value in number]
    elif isinstance(number, dict):
        return {key: value * value for key, value in number.items()}
    elif isinstance(number, set) or isinstance(number, frozenset):
        number1 = list(number)
        return set([value * value for value in number])
    else:
        return number * number

print(square(5) == 25) # True
print(square(5.2) == 27.040000000000003) # True
print(square([1,2,3]) == [1,4,9]) # True
print(square({1,2,3}) == set([1,2,3])) # True
print(square({'jack': 1, 'jill': 2, 'humpty': 3}) == {'jack': 1, 'jill': 4, 'humpty': 9}) # True
print(square(frozenset([1, 2, 3])) == frozenset([1, 4, 9])) # True
print(square(frozenset([1, 2, 3])) == frozenset([1, 4, 9])) # True
print(square(None)) # will raise the custom error message 'You gave a None type value.'