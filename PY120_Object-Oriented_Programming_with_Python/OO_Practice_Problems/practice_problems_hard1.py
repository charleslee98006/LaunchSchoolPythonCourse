# Question 1
# Ben and Alyssa are working on a vehicle management system. 
# So far, they have created classes called Auto and Motorcycle to represent automobiles and motorcycles. 
# After having noticed common information and calculations they were performing for each vehicle type, they decided to break the common behaviors into a separate class called WheeledVehicle. 
# This is what their code looks like so far:

# class WheeledVehicle:
#     def __init__(self,
#                  tire_list,
#                  kilometers_per_liter,
#                  liters_of_fuel_capacity):
#         self.tires = tire_list
#         self.fuel_efficiency = kilometers_per_liter
#         self.fuel_capacity = liters_of_fuel_capacity

#     def tire_pressure(self, tire_index):
#         self.tires[tire_index]

#     def inflate_tire(self, tire_index, pressure):
#         self.tires[tire_index] = pressure

#     def range(self):
#         return self.fuel_capacity * self.fuel_efficiency

# class Auto(WheeledVehicle):
#     def __init__(self):
#         # 4 tires with various tire pressures
#         super().__init__([30, 30, 32, 32], 50, 25.0)

# class Motorcycle(WheeledVehicle):
#     def __init__(self):
#         # 2 tires with various tire pressures
#         super().__init__([20, 20], 80, 8.0)

# Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:
    
# class Catamaran:
#     def __init__(self,
#                 number_propellers,
#                 number_hulls,
#                 kilometers_per_liter,
#                 liters_of_fuel_capacity):
        # ... code omitted ...
        
# This new class does not fit well with the object hierarchy defined so far. 
# Catamarans don't have tires. But we still want a common code to track fuel efficiency and range. 
# Modify the class definitions and move code into a mix-in, as necessary, to share code among the Catamaran and the wheeled vehicles.

class WheelsMaxIn:
    
    def tire_pressure(self, tire_index):
        self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure
    
class Vehicle:
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class Auto(WheelsMaxIn, Vehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__(50, 25.0)
        self.tire_list = [30, 30, 32, 32]

class Motorcycle(WheelsMaxIn, Vehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__(80, 8.0)
        self.tire_list = [20, 20]

class Catamaran(Vehicle):
    def __init__(self, num_propellers, num_hulls, fuel_efficiency, fuel_capacity):
        super().__init__(fuel_efficiency, fuel_capacity)
        self.num_propellers = num_propellers
        self.num_hulls = num_hulls
        
    def water_range(self):
        return super().range() + 10
        
        
class Motorboat(Catamaran):
    def __init__(self, fuel_efficiency, fuel_capacity):
        super().__init__(0,0,fuel_efficiency, fuel_capacity)


# Question 2
# Building on the prior question, we now must also track a basic motorboat. A motorboat has a single propeller and hull, but otherwise behaves similar to a catamaran. 
# Therefore, creators of Motorboat instances don't need to specify number of hulls or propellers. How would you modify the vehicles code to incorporate a new Motorboat class?
class Motorboat(Catamaran):
    def __init__(self, fuel_efficiency, fuel_capacity):
        super().__init__(0,0,fuel_efficiency, fuel_capacity)

# Question 3
# The designers of the vehicle management system now want to make an adjustment for how the range of vehicles is calculated. 
# For the seaborne vehicles, due to prevailing ocean currents, they want to add an additional 10km of range even if the vehicle is out of fuel.

# Alter the code related to vehicles so that the range for autos and motorcycles is still calculated as before, but for catamarans and motorboats, the range method will return an additional 10km.

class Catamaran(Vehicle):
    def __init__(self, num_propellers, num_hulls, fuel_efficiency, fuel_capacity):
        super().__init__(fuel_efficiency, fuel_capacity)
        self.num_propellers = num_propellers
        self.num_hulls = num_hulls
        
    def range(self):
        return super().range() + 10