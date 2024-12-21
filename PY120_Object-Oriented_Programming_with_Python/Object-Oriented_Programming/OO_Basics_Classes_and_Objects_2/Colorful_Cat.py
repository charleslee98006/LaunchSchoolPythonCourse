# Create a class named Cat that prints a greeting when the greet instance method is invoked. 
# The greeting should include the name and color of the cat. Use a class constant to define the color.

class Cat:
    
    def __init__(self, name, color):
        self._name = name
        self._color = color
    
    def greet(self):
        print(f'Hello! My name is {self._name} and I\'m a {self._color} cat!')
        
sophie = Cat('Sophie', 'purple')
sophie.greeting()