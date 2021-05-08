from unittest import TestCase
from game_cards.Card import Card

class TestCard(TestCase):
    def test_valid_card(self):
        card1 = Card("spade", 50)
        card2 = Card("spade","shalom")
        self.assertEqual(card1.value, None)
        self.assertTrue(card2.value, "Error")
