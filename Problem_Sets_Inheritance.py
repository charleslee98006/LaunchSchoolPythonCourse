# Class based inheritance works great when it's used to model hierarchical domains. 
#Let's take a look at a few practice problems. 
# Suppose we're building a software system for a pet hotel business, so our classes deal with pets.

#1. Given this class:

# class Dog:
#     def speak(self):
#         return 'bark!'

#     def sleep(self):
#         return 'sleeping!'

# class BullDog(Dog):

#     def __init__(self):
#         super().__init__()
    
#     def sleep(self):
#         return 'snoring!'

# teddy = Dog()
# bill = BullDog()
# print(teddy.speak())      # bark!
# print(teddy.sleep())       # sleeping!
# print(bill.speak())
# print(bill.sleep())

#2. Let's create a few more methods for our Dog class.

# class Pet:
#     def speak(self):
#         return 'bark!'

#     def sleep(self):
#         return 'sleeping!'

#     def run(self):
#         return 'running!'

#     def jump(self):
#         return 'jumping!'

# class Dog(Pet):

#     def fetch(self):
#         return 'fetching!'

# class Bulldog(Dog):
#    def sleep(self):
#        return "snoring!"

# class Cat(Pet):
    
#     def speak(self):
#         return 'meow!'
    
# # Create a new class called Cat, which can do everything a dog can, except fetch. 
# # Assume the methods do the exact same thing. 
# # Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.

# pet = Pet()
# dave = Dog()
# bud = Bulldog()
# kitty = Cat()

# print(pet.run())              # running!
# print(kitty.run())            # running!
# print(kitty.speak())          # meow!
# try:
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__, exception, "\n")
#     # AttributeError 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"

#4. What is the method resolution order and why is it important?
# The Method Resolution is a tree sequence of steps that Python takes to find the appropriate method and execute it. 
# It starts with the class the method resides before moveing up the parent hierarchy ladder. It is important because it shows
# how Python traverses throughout the program looking for the method to execute