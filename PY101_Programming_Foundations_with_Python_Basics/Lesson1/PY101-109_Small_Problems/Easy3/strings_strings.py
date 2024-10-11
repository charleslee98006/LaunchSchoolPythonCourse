def stringy(integer_length):
    if isinstance(integer_length, int):
        result = ''
        counter = 0
        while(counter < integer_length):
            if counter % 2:
                result += '0'
            else:
                result += '1'
            counter += 1
        return(result) 
    else:
        raise ValueError("Please use integer values only.")

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True