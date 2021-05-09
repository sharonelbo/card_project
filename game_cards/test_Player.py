from unittest import TestCase,mock
from game_cards.Player import Player
from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("sharon")
    def valid_player(self):
        self.assertTrue(self.player1.name == "sharon" and self.player1.num_of_cards == 12)


    def invalid_player(self):
        self.player1 = Player(111)
        self.assertEqual(self.player1.name, "player")
        self.player1 = Player("sharon", 200)
        self.assertEqual(self.player1.num_of_cards, 26)
        self.player1 = Player("sharon", -22)
        self.assertEqual(self.player1.num_of_cards, 0)
        self.player1 = Player(-1, -1)
        self.assertTrue(self.player1.name == "player" and self.player1.num_of_cards == 0)


    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, "club"))
    def test_valid_set_hand(self,mock):
        deck1 = DeckOfCards()
        player1 = Player("sharon", 1)
        player1.set_hand(deck1)
        self.assertIn(Card(1, "club"), player1._Player__hand)

    def test_get_card(self):
        pass
    def test_valid_add_card(self):
        card1 = Card(5,"club")
        self.player1.add_card(card1)
        self.assertIn(card1,self.player1._Player__hand)

    def test_invalid_add_card(self):
        self.player1.add_card("adsdad")
        self.assertNotIn("adsdad",self.player1._Player__hand)

    def test_get_card(self):
        player1 = Player("sharon")
        player1.add_card(Card(9,"diamond"))
        self.assertEqual(player1.get_card(),Card(9,"diamond"))
        self.assertEqual(0,len(player1._Player__hand))

    def test_get_invalid_card(self):
        player1 = Player("sharon")
        self.assertEqual(player1.get_card(),None)