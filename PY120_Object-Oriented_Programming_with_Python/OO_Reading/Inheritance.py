#1. For each of the following pairs of classes, try to determine whether they have an "is-a" or "has-a" relationship or neither.
# First Class	Second Class
# Car	Engine - Has-a relationship
# Teacher	Student - has-a
# Flag	Color Has-a relationship
# Apple	Orange - neither
# Ship	Vessel - ship is a vessel; vessel has a ship
# Structure	Home - Home has a structure
# Shape	Circle - circle is a shape; 

# Write the code needed to make the following code work as shown:
# class SignalMixIn:
    
#     def signal_left(self):
#         print(f'Signalling left')
    
#     def signal_right(self):
#         print(f'Signalling right')
    
#     def signal_off(self):
#         print(f'Signal is now off')

# class Vehicle():
    
#     count = 0
    
#     def __init__(self):
#         Vehicle.count += 1
    
#     @classmethod
#     def vehicles(cls):
#         return Vehicle.count
    
# class Car(SignalMixIn, Vehicle):
    
#     def __init__(self):
#         super().__init__()

# class Truck(SignalMixIn, Vehicle):
    
#     def __init__(self):
#         super().__init__()
        
# class Boat(Vehicle):
    
#     def __init__(self):
#         super().__init__()        

# print(Car.vehicles())     # 0
# car1 = Car()
# print(Car.vehicles())     # 1
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.vehicles())     # 4
# truck1 = Truck()
# truck2 = Truck()
# print(Truck.vehicles())   # 6
# boat1 = Boat()
# boat2 = Boat()
# print(Boat.vehicles())    # 8

#3. Create a mix-in for the Car and Truck classes from the previous exercise that lets you operate the turn signals: signal left, signal right, and signal off. Use the following code to test your code.

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# boat1.signal_left()      # AttributeError: 'Boat' object has no attribute 'signal_left'

# 4. Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.
# print(Car.mro())
# print(Truck.mro())
# print(Boat.mro())
# print(Vehicle.mro())

#5. We've provided new Car and Truck classes and some tests below. 
# Refactor them to use inheritance for as much behavior as possible. 
# The tests shown in the code should still work as shown:

class Vehicle:
    
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg
        
    def max_range_in_miles(self):
        return self.capacity * self.mpg               
        
class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck') # No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car') # No hookup_trailer method for Car