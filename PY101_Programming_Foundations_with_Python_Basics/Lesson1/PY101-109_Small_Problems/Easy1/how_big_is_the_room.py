def measure_room_area():
    width = input ('What is the width of the room in meters? ')
    length = input ('What about the length? ')
    if width.isnumeric() and length.isnumeric():
        if float(width) <= 0 or float(width) <= 0:
            print('User numerical value greater than zero!')
        else:
            area = float(width) * float(length)
            print(f'The area of the room is {area} square meters')
            print(f'The area of the room is {area * 10.7639} square feet')       
  
    else:
        print('Use enter numbers only')    


measure_room_area()
# Test Case 1: string value of 1 for width and length
# What is the width of the room in meters? 1
# What about the length? 1
# The area of the room is 1.0 square meters
# The area of the room is 10.7639 square feet

# Test Case 2: using string value with only alphabets
# What is the width of the room in meters? None
# What about the length? None
# Use enter numbers only

# Test Case 3: using string value with alphabets and numbers
# # What is the width of the room in meters? chuck8
# What about the length? 1t
# Use enter numbers only

# Test Case 4: using string value with zeroes
# # What is the width of the room in meters? 0
# What about the length? 0
# User numerical value greater than zero!