class Person:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

    def walk(self):
        return f'{self.name} {self.gait()} forward'

class Cat(Person):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(Person):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"