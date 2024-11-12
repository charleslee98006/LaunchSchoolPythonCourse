#P
# As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. 
# If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. 
# Both functions should return a value in the range 0 through 1439.
# Input:
#     - take the times in 24 hours (HH:RR) string format
# Output:
#     - return a integer value between 0 and 1439
# Explicit Rules:
#     - If the number of minutes is positive, the time is after midnight. 
#     - If the number of minutes is negative, the time is before midnight.
# Implicit Rules:
#     -
# Question:
#     - 
#E
# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

#D


#A
def after_midnight(string_time):
    string_list = string_time.split(":")
    hours = int(string_list[0]) * 60
    minutes = int(string_list[1])
    if(hours + minutes == 1440):
        return 0
    return hours + minutes

def before_midnight(string_time):
    string_list = string_time.split(":")
    hours = int(string_list[0]) * 60
    minutes = int(string_list[1])
    if(hours + minutes == 0):
        return 0
    return 1440 - (hours + minutes)

#C

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True