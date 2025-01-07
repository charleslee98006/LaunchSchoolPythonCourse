#Question 1
# Suppose you have these two classes:
# class Game:
#     def play(self):
#         return 'Start the game!'

# class Bingo(Game):
#     pass
# Update this code so that Bingo inherits the play method from the Game class.

#Question 2:

# Update your code from the previous question so the following code works as indicated:
# class Game:
#     count = 0
    
#     def __init__(self, game_name):
#         self._game_name = game_name
#         Game.count += 1
    
#     def play(self):
#         return f'Start the {self._game_name} game!'

# class Bingo(Game):
    
#     def __init__(self, game, name):
#         self.player_name = name
#         super().__init__(game)

# class Scrabble(Game):
    
#     def __init__(self, game, name, name2):
#         self.player_name1 = name
#         self.player_name2 = name2
#         super().__init__(game)
         

# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

#Question 3
# What are the benefits of using object-oriented programming in Python? Think of as many as you can.
# Easier mapping of real world behavior to what the program should do
# Each function and program would behave accordingly like in the real world
# categorization and organization is manage

#Question 4
# Suppose we have this code:
# class Greeting:
#     def greet(self, message):
#         print(message)

# class Hello(Greeting):
#     def hi(self):
#         self.greet('Hello')

# class Goodbye(Greeting):
#     def bye(self):
#         self.greet('Goodbye')

# # Without running the above code, what would each snippet do were you to run it?
# hello = Hello()
# hello.hi()
# # Instantiated the Hello class and assigned to `hello` variable; hello variable calls hi method, but calls the inherited greet method and prints hello

# hello = Hello()
# hello.bye()
# # Instantiated the Hello class and assigned to `hello` variable; hello variable calls bye method but resulted in the AttributeError because Goodbye Class's bye method is not inherited by Hello Class

# hello = Hello()
# hello.greet()
# # Instantiated the Hello class and assigned to `hello` variable; hello variable calls inherited greet() method, but returns an TypeError because greet method needs a method.

# hello = Hello()
# hello.greet('Goodbye')
# # Instantiated the Hello class and assigned to `hello` variable; hello variable calls inherited greet() method and print 'Goodbye'

# Hello.hi()
# Instantiated the Hello class and calls the inherited greet method and prints out `Hello` - Wrong
# This raises a TypeError because hi is missing one positional argument, for the self parameter. 
# This happens because we're invoking hi on the class Hello rather than an instance. When we invoke instance methods as class methods, no instance is passed in as self.

#Question 5
# Modify the code from the previous question so that Hello.hi() uses the Greeting.greet instance method to print Hi.
# class Greeting:
#     def greet(self, message):
#         print(message)

# class Hello(Greeting):
#     def hi():
#         Greeting.greet(Hello, 'Hi')

# Hello.hi()
# #Question 6
# # Consider the following code:
# class Cat:
#     def __init__(self, type):
#         self.type = type

# print(Cat('hairball'))
# # <__main__.Cat object at 0x10695eb10>

# The output here isn't very useful. It only tells us that we've got an instance of the Cat class, and it's memory address. 
# It would be better if the output were more meaningful. For instance, maybe it can print `I am a hairball`` instead. Update the code to produce that result.
# class Cat:
#     def __init__(self, type):
#         self.type = type
        
#     def __str__(self):
#         return f'I am a {self.type}'

# print(Cat('hairball')) # I am a hairball

#Question 7
# What would happen if you ran the following code? Don't run it until you've checked your answer:

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) #Amazon
print(tv.model()) # Omni Fire

print(Television.manufacturer()) #Amazon
print(Television.model()) # TypeError because it is missing the self argment