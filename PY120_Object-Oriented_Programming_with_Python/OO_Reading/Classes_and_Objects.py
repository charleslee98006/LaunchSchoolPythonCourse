# Create a Car class that meets these requirements:
    # Each Car object should have a model, model year, and color provided at instantiation time.
    # You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
    # Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
    # Create a method that prints a message about the car's current speed.
    # Write some code to test the methods.
    
# class Car:
        
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self._color = color
#         self.speed = 0
        
#     def turn_engine_on(self):
#         print(f'Engine turned on')

#     def turn_engine_off(self):
#         print(f'Engine turned off')
#         self.speed = 0

#     def accelerate(self, speed):
#         print(f'Accelerate by: {speed}')
#         self.speed += speed

#     def brake(self, speed):
#         print(f'Slowing down by: {speed}')
#         self.speed -= speed
        
#     def current_speed(self):
#         print(f'current speed: {self.speed}')

#     @property
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, color):
#         self._color = color
        
#     @property
#     def model(self):
#         return self._model
    
#     @model.setter
#     def model(self, model):
#         self._model = model
        
#     @classmethod
#     def avg_gas_mileage(cls, gallon, miles):
#         print(f'Gas mileage Average: { gallon / miles}')

# my_car = Car('Telsa', 'Model 3', 'Red')
# print(f'{my_car.model} {my_car.year} {my_car.color} ')

# my_car.turn_engine_on()
# my_car.accelerate(20)
# my_car.brake(10)
# my_car.current_speed()
# my_car.turn_engine_off()
# print(f'car color is: {my_car.color}')
# my_car.color = 'Green'
# print(f'car color is: {my_car.color}')
# print(f'car model is: {my_car.model}')
# my_car.model = 'Roadster'
# print(f'car model is: {my_car.model}')

# Car.avg_gas_mileage(40, 20.5)
class Person:

    def __init__(self, first_name, last_name):
        if isinstance(first_name, str) and isinstance(last_name, str) and first_name and last_name and first_name.isalpha() and last_name.isalpha():
            self._name = f'{first_name} {last_name}'
        else:
            raise ValueError('Name must be alphabetic.')
    
    @property
    def name(self):
        return f'{self._name.split()[0].capitalize()} {self._name.split()[1].capitalize()}'

    @name.setter
    def name(self, first_last_tuple):
        if(isinstance(first_last_tuple, tuple)) and first_last_tuple[0] and first_last_tuple[1] and first_last_tuple[0].isalpha() and first_last_tuple[1].isalpha():
            self._name = f'{first_last_tuple[0]} {first_last_tuple[1]}'
        else:
            raise ValueError('Name must be alphabetic.')
    def 

new_person = Person('joe', 'blow')
# incorrect_person = Person(123, 23123)
print(f'The fill name is: {new_person.name}')
new_person.name = ('jane', 'doe')
print(f'The fill name is: {new_person.name}')

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.