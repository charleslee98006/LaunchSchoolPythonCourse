def next_featured(number):
    if(number >=9876543201):
        return 'There is no possible number that fulfills those requirements.'
    else:
        counter = number // 7
        if counter % 2 == 0:
            counter -= 1 
        stop = False
        while not stop:
            new_number = counter*7
            is_unique = True
            for char in str(new_number):
                if str(new_number).count(char) > 1:
                    is_unique = False
                    break
            if new_number % 2 == 1 and new_number > number and is_unique:
                return new_number
            counter += 2
        print(new_list)


print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True