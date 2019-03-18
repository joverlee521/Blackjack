import unittest
import classes

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class TestClasses(unittest.TestCase):
    def test_card_string(self):
        card = classes.Card("Hearts", "Ace")
        result = str(card)
        self.assertEqual(result, "Ace of Hearts")
    def test_deck_shuffle(self):
        deck1 = classes.Deck()
        deck2 = classes.Deck()
        deck2.shuffle()
        self.assertIsNot(deck1, deck2) 
    def test_deck_deal(self):
        deck = classes.Deck()
        result = deck.deal()
        self.assertIs(type(result), classes.Card)
    def test_hand_add_normal_card(self):
        card = classes.Card("Hearts", "King")
        hand = classes.Hand()
        hand.add_card(card)
        self.assertIs(hand.cards[0], card)
        self.assertEqual(hand.value, 10)
        self.assertEqual(hand.aces, 0)
    def test_hand_add_ace_card(self):
        card = classes.Card("Hearts", "Ace")
        hand = classes.Hand()
        hand.add_card(card)
        self.assertIs(hand.cards[0], card)
        self.assertEqual(hand.value, 11)
        self.assertEqual(hand.aces, 1)
    def test_hand_adjust_for_ace_with_ace(self):
        hand = classes.Hand()
        hand.value = 31
        hand.aces = 1
        hand.adjust_for_ace()
        self.assertEqual(hand.value, 21)
        self.assertEqual(hand.aces, 0)
    def test_hand_adjust_for_ace_without_ace(self):
        hand = classes.Hand()
        hand.value = 31
        hand.aces = 0
        hand.adjust_for_ace()
        self.assertEqual(hand.value, 31)
        self.assertEqual(hand.aces, 0)
    def test_chips_make_bet(self):
        amount = 10
        chips = classes.Chips()
        chips.make_bet(amount)
        self.assertEqual(chips.bet, amount)
        self.assertEqual(chips.total, 100)
    def test_chips_win_bet(self):
        chips = classes.Chips()
        chips.bet = 10
        chips.win_bet()
        self.assertEqual(chips.total, 110)
        self.assertEqual(chips.bet, 0)
    def test_chips_lose_bet(self):
        chips = classes.Chips()
        chips.bet = 10
        chips.lose_bet()
        self.assertEqual(chips.total, 90)
        self.assertEqual(chips.bet, 0)

if __name__ == "__main__":
    unittest.main()