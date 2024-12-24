class Transform:
    
    def __init__(self, text):
        self._text = text
    
    def uppercase(self):
        return f'{self._text.upper()}'
    
    @classmethod
    def lowercase(cls, target_text):
        if isinstance(target_text, str):
            return target_text.lower()
        return NotImplemented

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz