from unittest import TestCase
from game_cards.Player import Player
from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards




class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("sharon",12)
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


    # @mock.patch('game_cards.Player.Player.deal_one', return_value= Card(1,"club"))
    # def test_set_hand(self):
    #     deck1 = DeckOfCards()
    #     self.player1.set_hand(deck1)
    #     self.assertIn("club", self.player1._hand)

    def test_get_card(self):
        pass
    def test_add_card(self):
        pass

    def test_get_hand(self):
        pass
