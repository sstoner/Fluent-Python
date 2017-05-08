"""
A Pythonic Card Deck 
demonstration magic methods
    __getitem__
    __len__
"""

import collections
Card = collections.namedtuple("Card",["rank","suit"])

class FrenchDeck():
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades,diamonds,clubs,hearts".split(",")

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks
                                       for suit in self.suits]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, item):    #该方法会向实例对象会返回一个list
        return self._cards[item]

deck = FrenchDeck()

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
from random import choice

#card = choice(deck)
#print(card)
#print(FrenchDeck.ranks.index(card.rank))

for card in sorted(deck,key=spades_high):
    print(card)

"""
special methods shouldn't often use in your code! user build-in methods    
"""