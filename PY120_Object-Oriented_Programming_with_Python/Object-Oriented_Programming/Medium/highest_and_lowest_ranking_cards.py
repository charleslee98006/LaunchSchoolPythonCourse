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
        self.suit = suit
        
    def __str__(self):
        return f'{self.rankConverter()} of {self.suit}'
    
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
    
    def __lt__(self, card):
        return self._rank < card._rank

    def __gt__(self, card):
        return self._rank > card._rank
    
    def __eq__(self, other_card):
        return self._rank == other_card._rank and self.suit == other_card.suit  
    
cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]

print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True