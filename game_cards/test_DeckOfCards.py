from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck1 = DeckOfCards()

    def test_valid_deck(self):
        self.assertEqual(len(self.deck1.deck), 52)

    def test_deal_one(self, ):
        self.assertTrue(type(self.deck1.deal_one()) == Card)
        self.assertNotIn(self.deck1.deal_one(), self.deck1.deck)
