import copy
data_set = {1, 2, 3, 4, 5}
copy_data_set = copy.copy(data_set)

for item in data_set:
    if item % 2 == 0:
        copy_data_set.remove(item)
        
print(copy_data_set)