from unittest import main
from unittest import TestCase
from unittest.mock import patch
import blackjack
import classes

class TestBlackjackFunctions(TestCase):
    @patch('builtins.input', return_value='10')
    def test_take_bets_int(self, input):
        chips = classes.Chips()
        self.assertEqual(blackjack.take_bets(chips), 10)
    
    def test_hit(self):
        deck = classes.Deck()
        hand = classes.Hand()
        blackjack.hit(deck, hand)
        self.assertEqual(len(deck.deck), 51)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(str(hand.cards[0]), "Ace of Clubs")
    
    

if __name__ == "__main__":
    main()