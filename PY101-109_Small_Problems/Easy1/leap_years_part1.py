def is_leap_year(year_date):
    if isinstance(year_date, int) or not(year_date <= 0):
        if year_date % 400 == 0:
            return True
        elif year_date % 100 == 0 and not(year_date % 400 == 0):
            return False
        elif year_date % 4 == 0 and not(year_date % 100 == 0):
            return True
        else:
            return False
    else:
        raise ValueError('Please use integers greater than zero for the argument.')

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)

print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)

print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)

print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)

print(is_leap_year(2025) == False)