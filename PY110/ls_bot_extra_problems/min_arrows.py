# #Problem
# -Input
#     - nested list of X,Y coordinates
# -Output
#     - min number of arrows burst all balloons
# -Explicit Rules
#     -Coordinates are inclusive
#     -arrows  can be shot up from anywhere on the number line
# -Implicit Rules

# #Examples

# # print(min_arrows([[10,16],[2,8],[1,6],[7,12]]) == 2) => [[10,11,12,13,14,15,16],[2,3,4,5,6,7,8], [1,2,3,4,5,6], 7,8,9,10,11,12]] =10, 2
# # print(min_arrows([[1,2],[3,4],[5,6],[7,8]]) == 4) => [[1,2],[3,4], [5,6], [7,8]], no overlaps at all hence, 4 shots needed
# # print(min_arrows([[1,2],[2,3],[3,4],[4,5]]) == 2) => [[1,2],[2,3],[3,4],[4,5]]; 2, 4
# # print(min_arrows([[1,5],[2,3],[3,4]]) == 1) => [[1,2,3,4,5],[2,3],[3,4]]
# # print(min_arrows([]) == 0)

# #Data structures
# - nested list of of all values
# - 
#Algo
# 1. Create a counter = 0 and index variable =0
# 2. get the range of all numbers inclusively
# 3. pop first list and compare with other lists has any numbers in other inner lists and increase the count by 1
#     1. if yes, remove the other inner list from the list

#Code
def ending_cord_sort(coordinates):
    return coordinates[1]
    
def min_arrows(list1):
    arrow_used = 0
    if not list1:
        return arrow_used
    current_arrow_position = -1
    for inner_list in sorted(list1, key=ending_cord_sort):
        if(inner_list[0] > current_arrow_position):
            arrow_used += 1
            current_arrow_position = inner_list[1]
    return arrow_used
    


print(min_arrows([[10,16],[2,8],[1,6],[7,12]]) == 2) #[[1,6],[2,8],[7,12],[10,16]]
print(min_arrows([[1,2],[3,4],[5,6],[7,8]]) == 4)
print(min_arrows([[1,2],[2,3],[3,4],[4,5]]) == 2)
print(min_arrows([[1,5],[2,3],[3,4]]) == 1)
print(min_arrows([]) == 0)