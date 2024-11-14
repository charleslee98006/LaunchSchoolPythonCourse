import random

is_player_turn = True
is_dealer_turn = False
is_game_running = True
players_hand = []
computers_hand = []
deck_of_cards = []

def play_twenty_one():
    print('Welcome to Black Jack!')
    while is_game_running:
        initial_setup()
        while is_player_turn:
            print("Player's Turn:\n")
            display_dealers_card(computers_hand[0])
            displays_all_card(players_hand)
            players_turn()
        while is_dealer_turn:
            print("Dealer's Turn: \n")
            displays_all_card(computers_hand)
            displays_all_card(players_hand)
            dealers_turn()
        dealer_player_compare_cards()
        play_again()
        
def play_again():
    gameover_screen = True
    while gameover_screen:
        play_again = input('Want to play again (Yes/No)? ').lower()
        if(play_again not in ['yes', 'no']):
            print('Invalid Input... Please try again')
        else:
            if play_again == 'no':
                print('Have a Good day!')
                exit()
            else:
                gameover_screen = False
                print('New Game....')
                global is_player_turn, is_dealer_turn, players_hand, computers_hand, deck_of_cards
                is_player_turn = True
                is_dealer_turn = False
                players_hand = []
                computers_hand = []
                deck_of_cards = []
    

def initial_setup():
    print('Setting up the game...')    
    creating_deck(deck_of_cards)
    draw_cards(players_hand, 2, deck_of_cards)
    draw_cards(computers_hand, 2, deck_of_cards)    

def draw_cards(hands_list, draw_number, deck_left):
        print(f'drawing {draw_number} cards...')    
        for index in range(0, draw_number):
            random_number = random.randint(0, len(deck_left)-1)
            card_drawn = deck_left.pop(random_number)
            hands_list.append(card_drawn)

def creating_deck(deck):
    for suite in ['HEARTS', 'SPADE', 'DIAMOND', 'CLUBS']:
        for value in range(1, 14):
            card = None
            if value == 1:
                card = [suite, 'ACE', 11]
            elif value > 10:
                if(value == 11):
                    card = [ suite, 'JACK', 10]
                elif(value == 12):
                    card = [ suite, 'QUEEN', 10]
                else:
                    card = [ suite, 'KING', 10]
            else:
                card = [ suite, str(value), value]
            deck.append(card)

def display_dealers_card(hands):
    print('Dealer visible Card:')
    print(f'{ hands[1]} of {hands[0]}')

def displays_all_card(hands):
    print("Player's Cards:")
    for index in range(len(hands)):
        print(f'{hands[index][1]} of {hands[index][0]}')

def players_turn():
    action = input('Do you want to hit, stay or quit? ').lower()
    print(f'You have chosen {action}')
    if action not in ['hit', 'stay', 'quit']:
        print('Invalid input...please try again...')
    elif action == 'hit':
        draw_cards(players_hand, 1, deck_of_cards)
    elif action == 'quit':
        print('Thank you for playing. Have a nice day!')
        exit()
    else:
        global is_player_turn, is_dealer_turn
        is_player_turn = False
        is_dealer_turn = True
    if(check_for_over_21(players_hand)):
        print('BUSTED! You went over 21. Gameover!')

def dealer_player_compare_cards():
    sum_players_hand = sum([card[2] for card in players_hand])
    sum_computer_hand = sum([card[2] for card in computers_hand])
    print(f"Dealer hand: {sum_computer_hand}\nPlayer's hand: {sum_players_hand}")
    if(sum_computer_hand > sum_players_hand):
        print('Dealer wins!')
    elif (sum_computer_hand < sum_players_hand):
        print('Player wins!')
    else:
        print('It is a tie!')


def check_if_under_17(hands):
    values_list = [card[2] for card in hands]
    return sum(values_list) < 17


def check_for_over_21(hands):
    print('This is the hand: ', hands)
    values_list = [card[2] for card in hands]
    sum_of_hand = sum(values_list)
    all_ace_value_changed = check_if_there_is_ace_not_changed(hands)
    if(sum_of_hand > 21 and not all_ace_value_changed):
        lower_ace_value(hands)
        sum_of_hand = sum([card[2] for card in hands])
        all_ace_value_changed = check_if_there_is_ace_not_changed(hands)
    return sum_of_hand > 21

def lower_ace_value(hand):
    for index in range(0, len(hand)):
        if hand[index][1] == 'ACE':
            hand[index][2] == 1
            
def check_if_there_is_ace_not_changed(hand):
    is_all_ace_one = True
    for index in range(0, len(hand)):
        if hand[index][1] == 'ACE' and hand[index][1] == 11:
            return False
                
def dealers_turn():
    is_under_17 = check_if_under_17(computers_hand)
    while(is_under_17):
        draw_cards(computers_hand, 1, deck_of_cards)
        displays_all_card(computers_hand)
        displays_all_card(players_hand)
        is_under_17 = check_if_under_17(computers_hand)
    if(check_for_over_21(computers_hand)):
        print('BUSTED! Dealer went over 21. You win!')
    else:
        global is_dealer_turn
        is_dealer_turn = False

play_twenty_one()