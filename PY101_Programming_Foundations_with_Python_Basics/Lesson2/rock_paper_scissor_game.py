import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f"==>{message}")
    
def rock_paper_scissors_game():
    exit = False
    computer_win_count = 0
    player_win_count = 0    
    while not exit:    
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input().lower()

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice. Please Try again!")

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {choice}, computer chose {computer_choice}")

        if ((choice == "rock" and computer_choice == "scissors") or
            (choice == "paper" and computer_choice == "rock") or
            (choice == "scissors" and computer_choice == "paper")):
            prompt("You win!")
        elif ((choice == "rock" and computer_choice == "paper") or
            (choice == "paper" and computer_choice == "scissors") or
            (choice == "scissors" and computer_choice == "rock")):
            prompt("Computer wins!")
        else:
            prompt("It's a tie!")
        
        while
        prompt("Want to continue (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            prompt("Thanks for playing! Have a good day!")
            exit = True
        else:
            prompt("That's not a valid choice. Please try again")
    
rock_paper_scissors_game()
