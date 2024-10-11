def multiply(number1, number2):
    if number1 == None and number2 == None:
        raise ValueError('You gave a None type value.')
    elif isinstance(number1, str) and isinstance(number2, str):
        number1 = float(number1)
        number2 = float(number2)
    elif isinstance(number1, list) and isinstance(number2, list):
        return [numberlist1 * numberlist2 for numberlist1, numberlist2 in zip(number1,number2)]
    elif isinstance(number1, dict) and isinstance(number2, dict):
        return {key: number1[key] * number2[key] for key in number1}
    elif isinstance(number1, set) and isinstance(number2, set):
        number1 = list(number1)
        number2 = list(number2)
        return set([numberlist1 * numberlist2 for numberlist1, numberlist2 in zip(number1,number2)])
    else:
        return number1 * number2

print(multiply(5, 3) == 15) # True
print(multiply([1,2,3], [6,5,33]) == [6, 10, 99]) # True

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15 }
print(multiply(prices, stock) == {"banana": 24, "apple": 0, "orange": 48, "pear": 45}) # True
print(multiply(set([1,2,3]), set([1,2,3])) == set([1,4,9])) # True
