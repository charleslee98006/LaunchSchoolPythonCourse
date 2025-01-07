#Question 1:
# Which of the following are objects in Python? If they are objects, how can you find out what class they belong to?

# 1. True - Not object
# 2. 'hello' - not objects
# 3. [1, 2, 3, 'happy days'] - objects; 
# 4. 142 - not object
# 5. {1, 2, 3} - object;
# 6. 1.2345 - not object; 


# to find out what class they belong to, you can use the type() method 
# print(type([1, 2, 3, 'happy days'] ))
# print(type({1,2,3}))

# True Answer: Every is an object. You can use the __class__.__name__ to get the class name

#Question 2:
# Suppose you have an AngryCat class that looks like this:
# class AngryCat:
#     def hiss(self):
#         print('Hisssss!!!')
        
# # How would you create a new instance of this class?

# cat = AngryCat()
# print(cat.hiss())

#Question 3:
# If we have a Car class and a Truck class and we want to be able to go_fast, how can we add the ability for them to go_fast using the mix-in SpeedMixin? 
# How can you check whether your Car or Truck can now go fast?
#answer:
# class SpeedMixin:
#     def go_fast(self):
#         print(f'I am a super fast {self.__class__.__name__}')

# class Car(SpeedMixin):
#     def go_slow(self):
#         print('I am safe and driving slow.')

# class Truck(SpeedMixin):
#     def go_very_slow(self):
#         print('I am a heavy truck and like going very slow.')

# # How to check:
# car = Car()
# truck = Truck()
# car.go_fast()
# truck.go_fast()

#Question 4:
# In the previous question, we had a mix-in called SpeedMixin that contained a go_fast method. We add this mix-in to the Car class as shown below:
# class SpeedMixin:
#     def go_fast(self):
#         print(f'I am a super fast {self.__class__.__name__}!')

# class Car(SpeedMixin):
#     def go_slow(self):
#         print('I am safe and driving slow.')

# small_car = Car()
# print(small_car.go_fast())
# # I am a super fast Car!

# #When we called small_car.go_fast, you may have noticed that the output includes the vehicle type. How is this done?
# # Since the Car class inherited the SpeedMixin, the car class also inherited the go_fast() method; therefore, when calling the print statement on line 55,
# # the self. part refers to the small_car instance object. The __class__ refers to the Car Class of small_car object, which subsequently retrieves the string name of the class through __name__

# #Question 5:
# # Which of the following classes would create objects that have an instance variable. How do you know?
# class Fruit:
#     def __init__(self, name):
#         my_name = name

# class Pizza:
#     def __init__(self, name):
#         self.my_name = name

# #Answer: Since instance variables are scoped to the object themselves and assigned to the objects themselves when created. Pizza class would create objects that 
# # has instance variable because of the `self` reference and assignment on line 77.
# # The Fruit class does not have instance variable because on line 73, `my_name` is treated as a local variable and is not assigned to self.

# pizza1 = Pizza('Cheese')
# print(pizza1.my_name)
# fruit1 = Fruit('Grape')
# print(fruit1.my_name) # Print out AttributeError because my_name is a local variable.

#Question 6
# Without running the following code, can you determine what the following code will do? Explain why you will get those results.
# import random

# class Oracle:
#     def predict_the_future(self):
#         return f'You will {random.choice(self.choices())}.'

#     def choices(self):
#         return [
#             'eat a nice lunch',
#             'take a nap soon',
#             'stay at work late',
#             'adopt a cat',
#         ]

# oracle = Oracle()
# print(oracle.predict_the_future())

# First, the Oracle class will be instantiated and initialized and assigned to the `oracle` variable on line 104.
# Second, the oracle call the `predict_the_future()` method. Before returning the f string, the random.choice will call the parameter function self.choices through function composition.
# since self is referencing to the oracle object, which is an Oracle class, the `choices` method returns the list of string options. 
# `Random.choice` will select an option from the list randomly and returns the f string.

# Question 7:
# Suppose you have the Oracle class and from above and a RoadTrip class that inherits from the Oracle class, as shown below:
# import random

# class Oracle:
#     def predict_the_future(self):
#         return f'You will {random.choice(self.choices())}.'

#     def choices(self):
#         return [
#             'eat a nice lunch',
#             'take a nap soon',
#             'stay at work late',
#             'adopt a cat',
#         ]

# class RoadTrip(Oracle):
#     def choices(self):
#         return [
#             'visit Vegas',
#             'fly to Fiji',
#             'romp in Rome',
#             'go on a Scrabble cruise',
#             'get hopelessly lost',
#         ]

# # What will happen when you run the following code?
# trip = RoadTrip()
# print(trip.predict_the_future())

# Instead of using Oracle class `choices` method, Python will use the RoadTrip class choices method and print out of one of the 5 options from line 131~135 randomly

# Question 8:
# Suppose you have an object named my_obj and that you want to call a method named foo using my_obj as the caller. 
# How can you see where Python will look for the method. 
# You don't need to determine the actual method location; just identifying the search sequence is sufficient.

#Answer: Search sequence will be the class that my_obj is first first. If not found, see if class has a parent and look in that class and again the same process but with the grandparent. 
# If none are found, it will finally look at the `Object` class and see before throwing AttributeError. all of this can be done with the .mro() method

#Question 9:
# There are several variables listed below. What are the different variable types and how do you know which is which?
# excited_dog = 'excited dog' - local or global variable type, depends on where it resides. 
# self.excited_dog = 'excited dog' - instance variable type because of `self` prefix
# self.__class__.excited_dog = 'excited dog' - class variable type because of self.__class__ prefix
# BigDog.excited_dog = 'excited dog' - Specifically BigDog Class variable type because BigDog is a class being referenced.

# Question 10:
# Suppose you have the following class:
class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

# Explain what the _cats_count variable is, what it does in this class, and how it works. Write some code to test your theory.

# Answer: the _cats_count variable is the Class variable. that keeps the total number of cats that has been created and initialized. 
# Every time a new Cat object is created, the Cat Class variable increments by 1. Hence, when user call the class method `cats_count`, 
# the class will return the class variable `_cats_count` number.

#Tests:
print(Cat.cats_count() == 0)
print(Cat._cats_count)
cat1 = Cat('orange')
print(Cat._cats_count)
cat2 = Cat('Blue')
cat2 = Cat('Green')
print(Cat.cats_count())