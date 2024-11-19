import datetime
#Problem
# Input
#     - Integer year
# Output
#     - number of Friday the 13th in that year.
# Explicit Rules
#     - Year is greater than 1752
# Implicit Rules
# Questions

#Example
# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

# Data Structures
# Algo
# Code
def friday_the_13ths(years):
    running_count = 0
    for month in range(1, 12): 
        days_in_a_month = (datetime.date(years, month+1, 1) - datetime.date(years, month, 1)).days
        for day in range(1, (days_in_a_month + 1)):
            day_during_iteration = datetime.datetime(years, month, day)
            if day_during_iteration !=None and day == 13 and day_during_iteration.weekday() == 4:
                running_count +=1
    return(running_count)
        
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True