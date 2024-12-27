# Include Card and Deck classes from the last two exercises.
import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank        
        if rank == 'Ace':
            self._rank = 14
        elif rank == 'Jack':
            self._rank = 11
        elif rank == 'Queen':
            self._rank = 12
        elif rank == 'King':
            self._rank = 13
        self._suit = suit
        
    def __str__(self):
        return f'{self.rankConverter()} of {self._suit}'
    
    def rankConverter(self):
        match self._rank:
            case 11:
                return 'Jack'
            case 12:
                return 'Queen'
            case 13:
                return 'King'
            case 14:
                return 'Ace'
            case _:
                return self._rank
    
    @property
    def rank(self):
        return self.rankConverter()
    
    @property
    def suit(self):
        return self._suit
    
    def __lt__(self, card):
        return self._rank < card._rank

    def __gt__(self, card):
        return self._rank > card._rank
    
    def __eq__(self, other_card):
        return self._rank == other_card._rank and self.suit == other_card.suit  

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self._deck = self._create_new_deck()
    
    def _create_new_deck(self):
        new_deck = []
        for suit_type in self.SUITS:
            for card_rank in self.RANKS:
                new_deck.append(Card(card_rank, suit_type))
        return new_deck
        
    def draw(self):
        if(len(self._deck) == 0):
            self._deck = self._create_new_deck()
        random_position = random.randint(0, len(self._deck)-1)
        return self._deck.pop(random_position)


class PokerHand:
    def __init__(self, deck):
        self._hand = []
        for _ in range(0, 5):
            self._hand.append(deck.draw())

    def print(self):
       print('Hand has: ')
       for card in self._hand:
           print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        for card in self._hand:
            # print(card.rank)
            # print(card.suit == 'Hearts')
            # print(card.rank in ['Ace', 'Queen', 'King', 'Jack'])
            if card.suit != 'Hearts':
                return False
            if  card.rank not in ['Ace', 'Queen', 'King', 'Jack', 10]:
                return False
        return True

    def _is_straight_flush(self):
        print('Flush')
        all_suit = self._hand[0].suit
        min_card = min(self._hand)
        max_card = max(self._hand)
        # print(min_card)
        # print(max_card)
        # print(min_card._rank)
        # print(max_card._rank)
        # print('len: ', len(list(range(min_card._rank, max_card._rank))))
        for card in self._hand:
            # print('Card Rank: ', card._rank)
            if card.suit != all_suit:
                return False
            if len(list(range(min_card._rank, max_card._rank+1))) != 5:
                return False
        return True

    def _is_four_of_a_kind(self):
        print('4Kind')
        tracker_dict = {}
        for card in self._hand:
            if tracker_dict.get(card.rank) == None:
                tracker_dict.setdefault(card.rank, 0)
            tracker_dict[card.rank] += 1
        for value in tracker_dict.values():
            if value == 4:
                return True
        return False
                

    def _is_full_house(self):
        print('Fullhouse')
        three_of_a_kind = False
        a_pair = False
        tracker_dict = {}
        for card in self._hand:
            if tracker_dict.get(card.rank) == None:
                tracker_dict.setdefault(card.rank, 0)
            tracker_dict[card.rank] += 1
        for value in tracker_dict.values():
            if value == 3:
                three_of_a_kind = True
            elif value == 2:
                a_pair = True
        return three_of_a_kind and a_pair

    def _is_flush(self):
        print('Flush')
        all_suit = self._hand[0].suit
        # print('SUIT: ', all_suit)
        for card in self._hand:
            # print('card suit: ', card.suit)
            if card.suit != all_suit:
                return False
        return True

    def _is_straight(self):
        print('Straight')
        tracker_dict = {}
        for card in self._hand:
            if tracker_dict.get(card.rank) == None:
                tracker_dict.setdefault(card.rank, 0)
            tracker_dict[card.rank] += 1
        for value in tracker_dict.values():
            if value != 1:
                return False
        if len(list(range(min(self._hand)._rank, max(self._hand)._rank+1))) == 5:
                return True
        return False

    def _is_three_of_a_kind(self):
        print('3ofKind')
        tracker_dict = {}
        for card in self._hand:
            if tracker_dict.get(card.rank) == None:
                tracker_dict.setdefault(card.rank, 0)
            tracker_dict[card.rank] += 1
        for value in tracker_dict.values():
            if value == 3:
                return True
        return False
        
    def _is_two_pair(self):
        print('2 pair!')
        pair1 = False
        pair2 = False
        card = False
        tracker_dict = {}
        for card in self._hand:
            if tracker_dict.get(card.rank) == None:
                tracker_dict.setdefault(card.rank, 0)
            tracker_dict[card.rank] += 1
        
        for value in tracker_dict.values():
            if value == 2 and pair1 == False:
                pair1 = True
            elif value == 2:
                pair2 = True
            elif value == 1:
                card = True
        return card and pair1 and pair2
                

    def _is_pair(self):
        print('Pair!')
        pair1 = False
        tracker_dict = {}
        for card in self._hand:
            if tracker_dict.get(card.rank) == None:
                tracker_dict.setdefault(card.rank, 0)
            tracker_dict[card.rank] += 1
        for value in tracker_dict.values():
            if value == 2:
                return True
        return False
        
    
    
# hand = PokerHand(Deck())
# hand.print()
# print(hand.evaluate())
# print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)

print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")