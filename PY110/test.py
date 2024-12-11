# DS
# lists - to get all combinations of list of digits

# Algo
 def bouncyCount(list1):
    1. Convert all of list1 into string version in a list
    2. created a counter = 0
    2. set up 1 boolean flag for ascending value = False
    3. set up 1 boolean flag for descending value = False
    4. go through each digit and see if:
        1. ascending - set flag to True 
        1. descending - set flag to True
    5. if both flag True increment count

def bouncyCount(list1):
    new_string_version_list = [ str(number) for number in list1 ]
    counter = 0
    
    for number in new_string_version_list:
        is_ascending = False
        is_descending = False
        for index in range(len(number)-1):
            if number[index] < number[index + 1]:
                is_ascending = True
            elif number[index] > number[index + 1]:
                is_descending = True
        if is_ascending and is_descending:
            counter += 1
    return counter


print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)