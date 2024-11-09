## Step 1: Understand the Problem
## Task 1
# Leftover Blocks
# You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

# The building blocks are cubes.
# The structure is built in layers.
# The top layer is a single block.
# A block in an upper layer must be supported by four blocks in a lower layer.
# A block in a lower layer can support more than one block in an upper layer.
# You cannot leave gaps between blocks.
# Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.

# Tasks
# You are provided with the problem description above. Your tasks for this step are:

# Make notes of your mental model for the problem, including:
# inputs and outputs.
# explicit and implicit rules.
# Write a list of clarifying questions for anything that isn't clear.

# inputs - a number of blocks
# output - number of leftover blocks

# explicit rules:
#     - structure is built on layers
#     - top layer is a single block
#     - lower layers can be support more than 1 block by upper layer
#     - No gaps between blocks
#     - upper layer must be supported by 4 blocks from lower layer
# implicit rules:
#     - Seems like there must be at least 3 layers. Need to confirm
#     - Seems like we will need 5 blocks at minimum.
#     - Need to lay down the lower layer first before laying on upper layers
# Questions:
#     - How are we to handle situations where there is less than 3 layers? Or no layers?
#     - Is there an importance of the blocks being cubed?
#     - What does the corner stone layer look like?

# Step 2: Examples and test cases
# You are provided with the following test cases for this problem.
#print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True
#
# Regarding your initial mental model and questions from Step 1, make some notes about the test cases. 
# Do the test cases confirm or refute different elements of your original analysis and mental model? 
# Do they answer any of the questions that you had, or do they perhaps raise further questions?

# Answer: they do refute my mental model and questions that I had about the problem. In particular,
# the implicit I came up with was wrong and I had to rethink about it as a pyramid shape. However, it does clarify the problem a lot more.

# Step 3: Data Structures
# For this step, use your analysis so far to make notes regarding whether you might need to 
# use any particular data structures as part of your solution. If so, make notes on which ones.

# My initial thoughts was going to the nested 2D array list as the nature of a pyramid goes from 1x1, 2x2, 3x3... NxN,
# but we might not need to use any data structures actually since we are working with square numbers to determine how many
# blocks we need to complete a pyramid structure.

# Step 4: Algorithm
# For this step, use your analysis of the problem so far to write out a high-level algorithm 
# that solves the problem at an abstract level. Avoid too much implementation detail at this stage.

# return_bricks function (number_of_bricks):
#     1. Starts with 1 bricks as the initial 
#     2. loop the following:
#         1. take the initial and square it 
#         2. take the squared value and add it to the initial
#         3. stop looping when the initial is greater or equal than the number of bricks
#     3. subtract the number of bricks with the initial to get the left over 
#     4. return the number of bricks left over

# Step 5: Implement a Solution in Code
#

def return_number_of_blocks(number_of_blocks):
    if(number_of_blocks == 0):
        return 0
    else:    
        initial_layer_number = 2
        count = 1
        while count < number_of_blocks:
            squared = initial_layer_number**2
            if(count + squared <= number_of_blocks):
                count += squared
                initial_layer_number += 1
            else:
                break
        return number_of_blocks - count

print(return_number_of_blocks(0) == 0)  # True
print(return_number_of_blocks(1) == 0)  # True
print(return_number_of_blocks(2) == 1)  # True
print(return_number_of_blocks(4) == 3)  # True
print(return_number_of_blocks(5) == 0)  # True
print(return_number_of_blocks(6) == 1)  # True
print(return_number_of_blocks(14) == 0) # True
print(return_number_of_blocks(100) == 9) # True