from unittest import TestCase,mock
from game_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck1 = DeckOfCards()

    def test_valid_deck(self):
        self.assertEqual(len(self.deck1.deck),52)

    @mock.patch("game_cards.DeckOfCards.DeckOfCards.random.randint", return_value=0)
    def test_deal_one(self):
        self.assertEqual(self.deck1.deal_one().value,1)
