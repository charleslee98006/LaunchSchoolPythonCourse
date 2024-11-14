data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for number in data:
    if(number not in unique_data):
        unique_data.append(number)
print(unique_data == [4, 2, 1, 3]) # order not guaranteed