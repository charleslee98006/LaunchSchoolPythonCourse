#P
# Input:
#     - floating point number repping an angle
# Output:
#     - 1 string with angles, minutes and seconds 
# Explicit Rules:
#     - input float is between 0 and 360
#     - minutes is rep by single quote
#     - seconds rep by double quote
#     - degree rep by unicode '\u00B0'
#     - 60 minutes in a degree
#     - 60 seconds in a minute 
# Implicit Rules:
#     - No need to account negative degrees
#     - will need tou output in string format
#     - implicit rules seems to use minutes and seconds to deal with leftover
# Question
#     - What does the format look like
#E

## All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"") .73
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

#D
# - Seems like it is a straight up conversion and formatting printing process no need for DS

#A
# def dms(angle):
#     1. take the angle and divide it by 60 and save the value to variable `minutes` to get angle in minutes
#     2. take the saved variable and multiply 60 and save the value to a variable `seconds` to get angle in seconds
#     3. string format  the seconds, angle and minutes variable values next to their corresponding the units of measure
#     4. return the results from step3
    
#C
import math

def dms(angle):
    leftover_in_minutes = (angle - int(angle)) * 60
    leftover_from_minutes = (leftover_in_minutes - int(leftover_in_minutes)) * 60
    degree_min_sec = f'{int(angle)}\u00B0{int(leftover_in_minutes):02}\'{int(leftover_from_minutes):02}"'
    return degree_min_sec

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
