import random
class GuessingGame:
    
    def __init__(self):
        self._number_of_guesses = 7
        
    def play(self):
        self._got_correct_number = False
        actual_number = random.randint(1, 100)
        while(self._number_of_guesses > 0):
            guess = int(input('Enter a number between 1 and 100: '))
            if self.validator(guess):
                self.is_right_number(guess,actual_number)
                self.game_over_check()
                    
    def validator(self, guess):
        if guess > 1 and guess < 100:
            return True
        print('Invalid Guess. ')
        return False
    
    def is_right_number(self, guess, actual_number):
        if guess == actual_number:
            print('That\'s the number!\n\nYou won!')
            self._number_of_guesses = 0
            self._got_correct_number = True
        elif guess < actual_number:
            print('Your guess is too low.')
            self._number_of_guesses -= 1
        elif guess > actual_number:
            print('Your guess is too high.')
            self._number_of_guesses -= 1
    
    def game_over_check(self):
        if not self._number_of_guesses and not self._got_correct_number:
            print('\nYou have no more guesses. You lost!')
            


game = GuessingGame()
game.play()