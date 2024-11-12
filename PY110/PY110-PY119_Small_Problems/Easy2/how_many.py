#P
# Write a function that counts the number of occurrences of each element in a given list. 
# Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

# Input:
#     -
# Output:
#     -
# Explicit Rules:
#     -
# Implicit Rules:
#     -
# Question:
#     - 
#E


#D


#A
def count_occurrences(list1):
    dictionary_occurrence = {vehicle: list1.count(vehicle) for vehicle in list1}
    print('# your output sequence may appear in a different sequence')
    for key, value in dictionary_occurrence.items():
        print(f'{key} => {value}')
#C

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)