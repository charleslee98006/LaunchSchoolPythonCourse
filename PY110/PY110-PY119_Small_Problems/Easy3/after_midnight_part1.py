#P
# The time of day can be represented as the number of minutes before or after midnight. 
# If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.
# Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input. 
#
# Input:
#     - any integer value
# Output:
#     - string of time of day in 24 hour format (hh:mm)
# Explicit Rules:
#     - The time of day can be represented as the number of minutes before or after midnight. 
#     - output needs to be in 24 hour (hh:mm)
#     - If the number of minutes is positive, the time is after midnight.
#     - If the number of minutes is negative, the time is before midnight.
#     - input is minutes based
# Implicit Rules:
#     - if at zero, => "00:00"
#     - 24 hours * 60  = 1440 minutes per day
# Question:
#     - 
#E
# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

#D
# none really; string formatting

#A
# def time_of_day(minutes):
    # 1. create a variable for hour
    # 2. create a variable for minutes
    # 3. divide minutes by 1440 to get the hour and assign it to hour variable
    #     - if over 24 hours, do modulo of the result by 24 and assign it to the hour variable
    # 4. do a modulo of the minutes by 60 to get the remainder and assign it to minute variable
#C
def time_of_day(minutes):
        hours = minutes % 1440 // 60
        minutes = round(((minutes % 1440 / 60) - hours)  * 60)
        return f'{hours:02d}:{minutes:02d}'
        
    
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True