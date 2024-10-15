# Question 1: Correct answer; but wrong explaination
# I believe it will return 2 different results because of the lazy sequencing on
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

# print(first())
# print(second())
#Answer: The block indentations with the expressions to return the same thing; 
# otherwise, second will return None

# Question 2:
# print(num_list) - prints out [1,2]
# print(dictionary) - prints out {'first': [1,2]}
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

# print(num_list)
# print(dictionary)


# Question 3: Mostly wrong with this one. Remember about scoping that reassignment 
# does not affect the values on outer scope values; if accessing the parameter values, we are mutating it; 
# hence, it would affect the the outer scope values.
# A) - mess_with_vars(["one"], ["two"],["three"])
#one = ["two"]
#two = ["three"]
#three = ["two"]
# Answer:
# one is: ["two"]
# two is: ["three"]
# three is: ["two"] 

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# B)
# Answer:
# one is: ["two"]
# two is: ["three"]
# three is: ["one"] 

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# C)
# Answer:
# one is: ["two"]
# two is: ["three"]
# three is: ["one"]

# def mess_with_vars(one, two, three):
#     one[0] = "two"
#     two[0] = "three"
#     three[0] = "one"

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# Question 4:
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if not len(dot_separated_words) == 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

# Question 5:
# I expect an error because because greeting variable will never run due to the if condition being always false

if False:
    greeting = "hello world"

print(greeting)
