# Question 1:
# Yes; it will raise an indexError because you are accessing 
# the sixth index when the numbers list contains only 3
# numbers = [1, 2, 3]
# numbers[6] = 5
# print(numbers)

# Question 2:
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
# print(str1.endswith('!'))
# print(str2.endswith('!'))
# Question 3:
famous_words = "seven years ago..."
prefix = "Four score and "
abs_quote1 = prefix + famous_words
# print(abs_quote1)
new_string = f"Four score and {famous_words}" # - totally forgot about this; remember
# print(new_string)

# Question 4:
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
# print(munsters_description.capitalize())

# Question 5: Remember!
# print(munsters_description.swapcase())

# Question 6:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
# print('Dino' in str1)
# print('Dino' in str2)

# Question 7:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')
# print(flintstones)

# Question 8:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones += ["Dino", "Hoppy"]
# print(flintstones)
# Question 9:
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
index = advice.index('house')
new_advice = advice[:index]
# print(new_advice)

# Question 10:
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))