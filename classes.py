# Imports
from random import shuffle
# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card():
    '''

    The Card class requires two inputs:
        suit(str): determines the suit of the card
        rank(str): used to determine the value of the card in a hand

    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    '''

    The Deck class does not require inputs.

    Attributes:
        deck(list): A list of all the cards in the deck

    '''

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        result = ""
        for card in self.deck:
            result += str(card) + ", "
        return result
    
    def shuffle(self):
        ''' Shuffles the deck using random.shuffle() '''
        shuffle(self.deck)
    
    def deal(self):
        ''' 
        
        Removes the last card of the deck 
        
        OUTPUT: the Card object that was removed from the list

        '''
        return self.deck.pop()

class Hand():
    '''
    The Hand class does not require inputs.

    Attributes:
        cards(list): list of all the cards in the hand
        value(int): the total value of the cards in the hand
        aces(int): the number of aces in the hand with value of 11

    '''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + ", "
        return result

    def add_card(self, card):
        '''

        Adds a Card object to the hand's card list.

        Adds the card's value to the hand's value.

        If the card is an Ace, add one to the hand's aces attribute

        INPUT: card(Card class): the Card object being added 

        '''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        ''' If the hand's value is over 21, adjust the value according to the number of aces '''
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips():
    '''
    
    The Chips class does not require inputs.
    
    Attributes:
        total(int): the total number of chips, initialized at 100
        bet(int): the amount the player bet 

    '''

    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def __str__(self):
        return f"You have a total of {self.total} chips."
    
    def make_bet(self, amount):
        ''' 
        
        Change the bet attribute according to the stated amount 
        
        INPUT: amount(int): the amount the player bet
        
        '''
        self.bet += amount

    def win_bet(self):
        ''' Add the bet to the total and reset bet to 0 '''
        self.total += self.bet
        self.bet = 0
    
    def lose_bet(self):
        ''' Subtract bet from the total and reset bet to 0 '''
        self.total -= self.bet
        self.bet = 0
