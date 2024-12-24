# Method Resolution Path (Part 1)

# Using the code below, determine the method resolution order (MRO) used when accessing the cat1.color property. 
# Only list the classes that are checked by Python when searching for the color attribute. Do not use the mro method.

# class Animal:
#     def __init__(self, color):
#         self._color = color

#     @property
#     def color(self):
#         return self._color

# class Cat(Animal):
#     pass

# class Bird(Animal):
#     pass

# cat1 = Cat('Black')
# print(cat1.color) # Cat -> Animal
# print(Cat.mro())

# Method Resolution Path (Part 2)
# Using the code below, determine the method resolution order (MRO) when accessing cat1.color. 
# Only list the classes and mix-ins Python will check when searching for the color method. Do not use the mro method.

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color # Cat -> Animal -> Object


# Method Resolution Path (Part 3)
# Using the code below, determine the method resolution order used when invoking bird1.color. 
# Only list the classes or mix-ins that Python will check when searching for the color method. Do not use the mro method.

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color) # Bird -> FlyingMixin -> Animal