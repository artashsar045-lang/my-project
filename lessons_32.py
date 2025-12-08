# Write a Python program to get the class name of an instance in
# Python.
# print(a.???) # output must be “A”
# class A:
#  pass
#
# a = A()
# print(a.__class__.__name__)

"""• Create a Deck of cards class.
 • The deck class should use another class, a Card class.
 • The Deck class should have a deal method to deal a single
 card from the deck. After a card is dealt, it is removed from
 the deck.
 • There should be a shuffle method which makes sure the
 deck of cards has all 52 cards and then rearranges them
 randomly.
 The Card class should have a suit (Hearts, Diamonds, Clubs,
 Spades) and a value (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)"""
# import random
#
# class Deck:
#     def __init__(self):
#         self.cards = []
#
#     def card_type(self):
#         self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
#         random.shuffle(self.cards)
#
#     def __len__(self):
#         return len(self.cards)
#
#     def __str__(self):
#         return len(self.cards)
#
#     def card_deal(self):
#         return self.cards.pop()
#
#
# class Card:
#     suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#     ranks = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
#     def __init__(self,suit,rank):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         return f"{self.rank} {self.suit}"
#
#
# d = Deck()
# d.card_type()
# print(len(d))
# card =d.card_deal()
# print(card)

"""• Create a Computation class with a default constructor (without parameters)
allowing to perform various calculations on integers numbers.
• Create a method called factorial() which allows to calculate the factorial of an
integer.
• Create a method called sum() allowing to calculate the sum of the first n
integers 1 + 2 + 3 + .. + n.
• Create a method called is_prime() allowing to test the primality of a given
integer.
• Create a method called all_is_prime() allowing to display all prime integer
numbers from 2 to n.
• Create a table_mult() method which creates and displays the multiplication
table of a given integer (from 1 to 10).
• Then create an all_tables_mult() method to display all the integer
multiplication tables (from 1 to 10)"""
