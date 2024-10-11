def century(year):
    century_years = 0
    suffix = ''
    if(year <= 100):
        century_years = 1
    elif(year % 100 >= 1):
        century_years = (year // 100 + 1)
    else:
        century_years = year // 100
    if(century_years % 100 >= 11 and century_years % 100 <= 19 ):
        suffix = 'th'
    elif(str(century_years).endswith('1')):
        suffix = 'st'
    elif(str(century_years).endswith('2')):
        suffix = 'nd'
    elif(str(century_years).endswith('3')):
        suffix = 'rd'
    else:
        suffix = 'th'
    return f'{century_years}{suffix}'

print(century(2401) == "25th")          # True
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True