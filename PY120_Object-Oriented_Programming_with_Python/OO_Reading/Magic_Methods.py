# # 1. Create a Car class that makes the following code work as indicated:
# class Car:
    
#     def __init__(self, id, year, color):
#         self.id = id
#         self.year = year
#         self.color = color
    
#     def __str__(self):
#         return f'{self.id} {self.year} {self.color}'
    
#     def __repr__(self):
#         return f'Car({repr(f'{self.id}, {self.year}, {self.color}')})'


# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

#2. Earlier, we wrote the following class:

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)
    
#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplmented
#         new_x = self.x - other.x
#         new_y = self.y - other.y
#         return Vector(new_x, new_y)
    
#     def __mul__(self, other):
#         return (self.x * other.x) + (self.y * other.y)
    
#     def __abs__(self):
#         return ((self.x**2) + (self.y**2))**0.5

#     # __iadd__ method omitted; we don't need it for this exercise

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)

# # Update this class so the following code works as indicated:

# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

# Challenge: Create the classes needed to make the following code work as shown:

class Candidate:
    
    def __init__(self, name):
        self.name = name
        self._votes = 0
    
    def __iadd__(self, votes):
        if not isinstance(votes, int):
            return NotImplemented
        self._votes += votes
    
    @property
    def votes(self):
        return self._votes
    
    @votes.setter
    def setter(self, votes):
        self._votes = votes
    
class Election:
    
    def __init__(self, candidates):
        self.candidates = candidates
    
    def results(self):
        total = 0
        result_dict = {}
        for candidate in candidates:
            print(f'{candidate.name}: {candidate.votes} votes')
            total += candidate.votes
            result_dict[candidate.name] = candidate.votes
        sorted_dict = sorted(result_dict.items(), key=lambda x: -x[1])
        print(f'{sorted_dict[0][0]} won: {sorted_dict[0][1] / total *100 :.1f}% of votes' )


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1 # this is essentially candidate = candidate + 1

election = Election(candidates)
election.results()