# 1. Define a Dog class that has a breed instance variable. 
# Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. 
# Print the breed of each dog.
# class Dog:
#     def __init__(self, breed):
#         self.breed = breed

# golden = Dog('Golden')
# poodle = Dog('Poodle')
# print(golden.breed)
# print(poodle.breed)

# 2. Add a get_breed method to the Dog class from your answer to the previous problem. 
# The method should return the dog's breed. Use the method to print the breeds of the two dog objects you created in the previous problem. 
# You should also mark the breed instance variable for internal use only.

# class Dog:
#     def __init__(self, breed):
#         self._breed = breed
        
#     def get_breed(self):
#         return self._breed

# golden = Dog('Golden')
# poodle = Dog('Poodle')
# print(golden.get_breed())
# print(poodle.get_breed())

# 3. Create a Cat class that has a single method named get_name that returns the name instance variable. 
# Without initializing name, try to instantiate a Cat object and call get_name. Print Name not set! when the error occurs.

# class Cat:
#     def get_name(self):
#         try:
#             return self.name
#         except AttributeError:
#             return 'Name not set!'
            
# cat = Cat()
# print(cat.get_name())

#4. Create an instance of the Dog class from your answer to Problem 2. 
# Set its breed directly from outside the class, then print the resulting breed.

# class Dog:
#     def __init__(self, breed):
#         self._breed = breed
        
#     def get_breed(self):
#         return self._breed

# poodie = Dog('Poodle')
# poodie._breed = 'Goldie'
# print(poodie.get_breed())

# 5. Define a Student class that has a class variable named school_name. You should initialize the school name to 'Oxford'. 
# After defining the class, instantiate an instance of the Student class and print the school name using that instance.
# class Student:
#     school_name = 'Oxford'
    
# school = Student()
# print(school.school_name)
# print(school.__class__.school_name)
        
# 6.Modify the Student class from your answer to the previous problem. The modified class should have an instance variable called name that gets initialized during instantiation. 
# Create two Student objects with different names but the same school, then print the name and school for both students.
# class Student:
#     school_name = 'Oxford'
    
#     def __init__(self, name):
#         self.name = name
    
# charlie = Student('Charlie')
# bob = Student('Bob')
# print(f'{charlie.name} {charlie.__class__.school_name}')
# print(f'{bob.name} {bob.__class__.school_name}')

# 7. Modify the Student class from your answer to the previous problem. The modified class should have a class method that returns the school's name. 
# Without instantiating any Student objects, print the school's name in two different ways: once with the class method, and once by accessing the class variable directly.

# class Student:
#     school_name = 'Oxford'
    
#     def __init__(self, name):
#         self.name = name
        
#     @classmethod
#     def get_school_name(cls):
#         return cls.school_name
    
# print(Student.get_school_name())
# print(Student.school_name)

# 8. Create a Car class that has a class variable named manufacturer and an instance variable named manufacturer. 
# Initialize these variables to different values. Add a show_manufacturer method that prints both the class and instance variables.
# class Car:
#     manufacturer = 'Honda'
    
#     def __init__(self, manufacturer):
#         self.manufacturer = manufacturer
    
#     def show_manufacturer(self):
#         return f'{self.__class__.manufacturer} {self.manufacturer}'

# car = Car('Toyota')
# print(car.show_manufacturer())

# 9. Create a Bird class that has a species attribute. Create a Sparrow class that inherits from the Bird class. 
# Create a Sparrow instance object, then print its species. The expected output is sparrow.

# class Bird:
    
#     species = ''
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     pass

# sparrow = Sparrow('sparrow')
# print(sparrow.species)

#10. Consider the following:
# class Bird:
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     def __init__(self, species, color):
#         self.color = color

# birdie = Sparrow("sparrow", "brown")
# print(birdie.species)               # What will this output?

#This code will raise an AttributeError since the Sparrow class doesn't initialize the species instance variable. To fix this problem, we must call Bird.__init__ from inside Sparrow.__init__:

#11. Create a Mammal class that always sets an attribute called legs to a value of 4. 
# Create a Human class that inherits from Mammal, but instead sets the value of legs to 2. Print the number of legs for a human to verify correct operation.

# class Mammal:
#     legs = 4
    
# class Human(Mammal):
#     legs = 2
    
# print(Human.legs)
# print(Mammal.legs)

# 12. the answer is `roar` because though it found the method from the Cat class, the class is Lion hence, it will make roar 
# 13. the answer is that pine will have `type` attribute to be 'Pine Tree' because though the super is initialized, the last line overrides the previous attribute with a new value
# class Tree:
#     def __init__(self):
#         self.type = "Generic Tree"

# class Pine(Tree):
#     def __init__(self):
#         super().__init__()
#         self.type = "Pine Tree"
# print(Pine().type)

# 14. My answer is that there would be an AttributeError stating that var_a is not found because though class B inherits class A, The variables do not; only the methods are inherited. Will need super().init() 
# to initialized var_a
class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        super().__init__()
        self.var_b = "B class variable"

b = B()
print(b.var_a)