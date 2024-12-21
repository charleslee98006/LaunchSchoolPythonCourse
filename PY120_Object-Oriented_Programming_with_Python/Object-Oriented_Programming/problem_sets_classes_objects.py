#1. Given the following code, create the Person class needed to make the code work as shown:
# class Person:
    
#     def __init__(self, name):
#         self.name = name
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         self._name = name

# bob = Person('bob')
# print(bob.name)           # bob
# bob.name = 'Robert'
# print(bob.name)           # Robert

#2. Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.
# class Person:
    
#     def __init__(self, first_name):
#         self.first_name = first_name
#         self.last_name = ''


#     @property
#     def first_name(self):
#         return self._first_name
    
#     @first_name.setter
#     def first_name(self, first_name):
#         self._first_name = first_name

#     @property
#     def last_name(self):
#         return self._last_first_name
    
#     @last_name.setter
#     def last_name(self, last_name):
#         self._last_first_name = last_name

#     @property
#     def name(self):
#         return self.first_name + ' ' + self.last_name

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# 3. Add a new setter property for name that takes either a first name or full name, and knows how to set the first_name and last_name properties appropriately. 
# Use the following code to test your code:

# class Person:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return f'{self.first_name} {self.last_name}'.strip()

#     @name.setter
#     def name(self, name):
#         first_and_last = name.split()
#         self.first_name = first_and_last[0]
#         self.last_name = ''
#         if len(first_and_last) > 1:
#             self.last_name = first_and_last[1]
            
#     @property
#     def first_name(self):
#         return self._first_name

#     @first_name.setter
#     def first_name(self, first_name):
#         self._first_name = first_name

#     @property
#     def last_name(self):
#         return self._last_name

#     @last_name.setter
#     def last_name(self, last_name):
#         self._last_name = last_name
        
# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# bob.name = 'Prince'
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''

# bob.name = 'John Adams'
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams

#4. Using the class definition from problem 3, let's create some more people (Person objects):

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, name):
        first_and_last = name.split()
        self.first_name = first_and_last[0]
        self.last_name = ''
        if len(first_and_last) > 1:
            self.last_name = first_and_last[1]
            
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    def __str__(self):
        return self.name

# bob = Person('Robert Smith')
# rob = Person('Robert Smith')
# print(bob.name.__eq__(rob.name))

#5. Continuing with our Person class definition, what do you think the following code prints?

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")