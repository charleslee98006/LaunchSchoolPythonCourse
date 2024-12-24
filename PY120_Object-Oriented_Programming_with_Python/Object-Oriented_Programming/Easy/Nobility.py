class WalkMixIn:
    
    def walk(self):
        return f'{self.name} {self.gait()} forward'

class Noble(WalkMixIn):
    
    def __init__(self, name, title):
        self._name = name
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @property
    def name(self):
        return self._name
    
    def gait(self):
        return "struts"
        

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"
