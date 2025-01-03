#1.Name the method used to customize each of the following operators:
# > - __gt__
# * - __mul__
# <= - __le__
# != - __ne__
# += -  __iadd__
# **= - __ipow__
# // - __floordiv__

#2. 
# class Cat:
#     def __init__(self, name):
#         self.name = name.lower()

#     def __eq__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name == other_cat.name.lower()
    
#     def __ne__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name != other_cat.name.lower()
    
# bob = Cat('BOB')
# bob2 = Cat('bob')
# robert = Cat('Robert')
# jack = Cat('Jack')
# print(bob == bob2) #True
# print(bob != bob2) #False
# print(jack == robert) #False
# print(jack != robert) #True
# print(bob == 'Bob') #False
# print(bob != 'Bob') # True

#3.
# class Cat:
#     def __init__(self, name):
#         self.name = name.casefold()

#     def __eq__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name == other_cat.name.casefold()
    
#     def __ne__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name != other_cat.name.casefold()
    
#     def __lt__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name < other_cat.name.casefold()
    
#     def __le__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name <= other_cat.name.casefold()
    
#     def __gt__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name > other_cat.name.casefold()
    
#     def __ge__(self, other_cat):
#         if not isinstance(other_cat, Cat):
#             return NotImplemented
#         return self.name >= other_cat.name.casefold()
    
# bob = Cat('BOB')
# bob2 = Cat('bob')
# robert = Cat('Robert')
# jack = Cat('Jack')
# print(bob > bob2) #True
# print(bob >= bob2) #False
# print(bob < bob2) #True
# print(bob <= bob2) #False

# 4.
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'Vector({self.x}, {self.y})'
    
#     def __add__(self, another_vector):
#         if not isinstance(another_vector, Vector):
#             return NotImplemented
#         return Vector(self.x + another_vector.x, self.y + another_vector.y)
    
#     def __sub__(self, another_vector):
#         if not isinstance(another_vector, Vector):
#             return NotImplemented
#         return Vector(self.x - another_vector.x, self.y - another_vector.y)

#     def __mul__(self, number):
#         if not isinstance(number, int):
#             return NotImplemented
#         return Vector(self.x * number, self.y * number)

#     def __rmul__(self, number):
#         return self.__mul__(number)

# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)
# print(my_vector)                      # Vector(8, 16)

# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5) # TypeError: unsupported operand type(s) for +: 'Vector' and 'int'

# 5. 
class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    def __add__(self, text):
        if(isinstance(self.value, int) and isinstance(text, int)):
            return Silly(self.value + text)
        elif str(self.value).isnumeric() and str(text).isnumeric():
            return Silly(int(self.value) + int(text))
        else:
            return Silly(str(self.value) + str(text))
        

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)