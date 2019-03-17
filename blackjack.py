# Imports
from classes import Deck, Hand, Chips

# Global variables
playing = True

def take_bets(chips):
    '''

    Asks player for bet amount.

    Verifies player input is an int and does not exceed the amount the player currently has.
    
    INPUT: chips(Chips class): the player's Chip object

    OUTPUT: new_bet(int): the amount the player bet

    '''
    while True:
        try:
            new_bet = int(input("Enter your bet: "))
        except:
            print("Please enter positive integers only")
            continue
        else:
            if new_bet < 0: 
                print("Please enter positive numbers only!")
                continue
            elif new_bet > chips.total:
                print("Do not bet more than what you have! " + str(chips))
                continue
            elif new_bet == 0:
                print("There's no free games! You need to make a bet!")
                continue
            else:
                break
    return new_bet

def hit(deck, hand):
    '''

    Deals one card from the deck to the hand

    Will adjust the hand for Aces if necessary

    INPUT:
        deck(Deck class): the current Deck object
        hand(Hand class): the hand object (player or dealer)

    '''
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    '''

    Asks the player to hit or stand.

    Will deal card to player's hand if player selects 'hit'

    Will break out of the playing loop if player selects 'stand'

    INPUT:
        deck(Deck class): the current deck obj
        hand(Hand class): the player's hand obj

    '''
    global playing
    while True:
        player_choice = input("Hit or Stand?: ").lower()
        if player_choice == "hit":
            hit(deck, hand)
            break
        elif player_choice == "stand":
            playing = False
            break

def show_hands(player, dealer, hidden = True):
    '''

    Prints out the player's hand and the dealer's hand

    INPUT:
        player(Hand class): the player's hand obj
        dealer(Hand class): the dealer's hand obj
        hidden(bool): if True, hide dealer's first card

    '''
    player_hand = ""
    dealer_hand = ""
    for card in player.cards:
        player_hand += str(card) + "; "
    if hidden:
        for card in dealer.cards[1:]:
            dealer_hand += str(card) + ";"
        print(f"Dealer hand: Hidden Card; {dealer_hand}")
    else: 
        for card in dealer.cards:
            dealer_hand += str(card) + ";"
        print(f"Dealer hand: {dealer_hand}")
    print(f"Player hand: {player_hand}")
    
def show_all(player, dealer):
    '''

    Prints the player and dealer's hands and their final values

    INPUT:
        player(Hand class): the player's hand obj
        dealer(Hand class): the dealer's hand obj

    '''
    show_hands(player, dealer, False)
    print("Revealing final hands: ")
    print(f"Dealer hand value: {dealer.value}\nPlayer hand value: {player.value}")

def player_busts(chips):
    ''' 
    
    Tells player they have busted.

    Runs chips.lose_bet()

    INPUT: chips(Chips class): the player's chips obj

    '''
    chips.lose_bet()
    print("Oh no! You busted!")

def player_wins(chips):
    '''

    Tells player they have won.

    Runs chips.win_bet()

    INPUT: chips(Chips class): the player's chips obj

    '''
    chips.win_bet()
    print("Congratulations! You won!")

def dealer_busts(chips):
    '''

    Tells the player the dealer busted

    Runs player_wins()

    INPUT: chips(Chips class): the player's chips obj

    '''
    print("The dealer busted!")
    player_wins(chips)

def dealer_wins(chips):
    '''

    Tells the player the deal has won.

    Runs chips.lose_bet()

    INPUT: chip(Chips class): the player's chips obj

    '''
    print("The dealer won! Better luck next time!")
    chips.lose_bet()

def push(chips):
    '''

    Tells the player it was a push(tie)

    Resets player's bet to 0.

    INPUT: chip(Chips class): the player's chips obj

    '''
    chips.bet = 0
    print("It's a push!")

def replay():
    '''
    Asks player if they want to play again
    INPUT: none, takes input from console
    OUTPUT: boolean(True = play again)
    '''
    response = input("Would you like to play again? (Y/N): ").upper()
    if response != "Y" and response != "N":
        return replay()
    return response == "Y"

if __name__ == "__main__":
    # Initializing the player's chips
    player_chips = Chips()
    while True:
        print("Welcome to Blackjack!")
        # Initializing the deck, the player's hand, the dealer's hand
        deck = Deck()
        deck.shuffle()
        dealer = Hand()
        player = Hand()
        print(player_chips)
        # Asking player for the amount they want to bet
        bet = take_bets(player_chips)
        player_chips.make_bet(bet)
        # Dealing two cards to the player and the dealer
        for _ in range(2):
            hit(deck, player)
            hit(deck, dealer)
        # Printing out the current hands
        show_hands(player, dealer)
        # Enter play time!
        while playing:
            # Asking player to hit or stand
            hit_or_stand(deck, player)
            show_hands(player, dealer)
            if player.value > 21:
                player_busts(player_chips)
                break
        if player.value <= 21:
            print("The dealer is playing...")
            while dealer.value < 17:
                hit(deck, dealer)
            show_all(player, dealer)
            if dealer.value > 21:
                dealer_busts(player_chips)
            elif dealer.value <= 21:
                if player.value == 21 and dealer.value != 21:
                    player_wins(player_chips)
                elif dealer.value == 21 and player.value != 21:
                    dealer_wins(player_chips)
                else:
                    if dealer.value > player.value:
                        dealer_wins(player_chips)
                    elif player.value > dealer.value:
                        player_wins(player_chips)
                    elif player.value == dealer.value:
                        push(player_chips)
        print(player_chips)
        if(player_chips.total == 0):
            print("You are out of chips! Goodbye!")
            break
        if replay():
            playing = True
        else:
            break