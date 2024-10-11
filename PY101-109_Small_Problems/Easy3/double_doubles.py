def twice(number):
    if(isinstance(number, int)) and number >= 10:
        str_version = str(number)
        return number if(not(len(str_version) % 2)) and (
            str_version[0 : (len(str_version) // 2)] == 
            str_version[len(str_version) // 2 : len(str_version)]) else number * 2
    else:
        raise ValueError('Please use positive double digit integers only.')
    

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True