from unittest import TestCase
from game_cards.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(5,"diamond")

    def test_valid_card(self):
        self.assertEqual(self.card1.value,5)
        self.assertEqual(self.card1.suit,"diamond")

    def test_invalid_value(self):
        self.card1 = Card(14,"diamond")
        self.assertNotEqual(self.card1.value,14)
        self.card1 = Card(-1, "diamond")
        self.assertEqual(self.card1.value, None)
        self.card1 = Card("*AS", "diamond")
        self.assertEqual(self.card1.value, None)

    def test_invalid_suit(self):
        self.card1 = Card(1, "adsdsa#")
        self.assertNotEqual(self.card1.suit, "adsdsa#")
        self.assertEqual(self.card1.suit, None)
        self.card1 = Card(1, 9.5)
        self.assertEqual(self.card1.suit, None)

    def test_invalid_card(self):
        self.card1 = Card(9.5, "abc")
        self.assertTrue(self.card1.value is None and self.card1.suit is None)

    def test_gt(self):
        card2 = Card(1,"heart")
        card3 = Card(13,"diamond")
        self.assertTrue(card2 > card3)
        card2 = Card(12, "heart")
        self.assertTrue(card2 < card3)
        card3 = Card(12, "diamond")
        self.assertTrue(card2 > card3)
        self.card1 = Card(15, "sdda")
        self.card2 = Card(-1, "fddfsdf")
        self.assertTrue((self.card1 > self.card2) is None)

    def test_eq(self):
        card1 = Card(1, "heart")
        card2 = Card(1, "heart")
        self.assertTrue(card1 == card2)
        card1 = Card(1, "heart")
        card2 = Card(1, "diamond")
        self.assertFalse(card1 == card2)
        card1 = Card(2, "heart")
        card2 = Card(3, "heart")
        self.assertFalse(card1 == card2)
        card1 = Card(1, 1)
        card2 = Card(1, "heart")
        self.assertEqual(card1 == card2,None)
