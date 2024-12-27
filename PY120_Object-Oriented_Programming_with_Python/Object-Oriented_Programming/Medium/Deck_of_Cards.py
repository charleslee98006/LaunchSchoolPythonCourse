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
    
deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).