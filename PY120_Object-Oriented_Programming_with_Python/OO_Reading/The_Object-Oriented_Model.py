#How do we create a class and an object in Python?
#Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable 
# that gets initialized by the initializer.
#What class you create doesn't matter, provided it satisfies the above requirements.


class Car:
    
    def __init__(self, name):
        self.name = name
        print(f'Naming car as {self.name}')
    
    def going_to(self, destination):
        print(f'Driving to: {destination}')

toyota = Car('Toyota')
toyota.going_to('Home')

#Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.
1. through the initialized method or through the Foo object class initialization process

Answer:
    
class Foo:
    pass

foo = Foo()
print(f'I am a {type(foo).__name__} object')
print(f'I am a {foo.__class__.__name__} object')