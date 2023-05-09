# Part 1 : Quizz :
# Answer the following questions
#
# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?
#
#
# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
#
# The requirements are as follows:
#
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:

    SUITS = ['CLUB', 'DIAMOND', 'Heart', 'SPADE']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = []
        self.shuffle()
        
    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(suit, rank))

        shuffle(self.cards)


if __name__ == '__main__':
    deck = Deck()
