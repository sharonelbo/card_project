from unittest import TestCase
from game_cards.CardGame import CardGame


class TestCardGame(TestCase):
    def test_valid_game(self):
        game1 = CardGame("sharon", "avi")
        self.assertEqual("sharon", game1.players[0].name)
        self.assertEqual("avi", game1.players[1].name)
        self.assertEqual(10,game1.players[0].num_of_cards)

    def test_invalid_game(self):
        game1 = CardGame(23,9.6,9000)
        self.assertEqual("player1", game1.players[0].name)
        self.assertEqual("player2", game1.players[1].name)
        self.assertNotEqual(9000, game1.players[1].num_of_cards)
        game1 = CardGame(23, 9.6, {1:2})
        self.assertEqual(10, game1.players[1].num_of_cards)

    def test_valid_new_game(self):
        game1 = CardGame("sharon","avi",10)
        game1.new_game()
        self.assertEqual(len(game1.players[0]._Player__hand), 10)
        self.assertEqual(len(game1.players[1]._Player__hand), 10)
        self.assertEqual(game1._CardGame__started, True)


    def test_get_winner(self):
        game1 = CardGame("sharon","avi",10)
        game1.new_game()
        game1.players[0]._Player__hand = []
        self.assertEqual(game1.get_winner(),game1.players[0])
        game1.players[1]._Player__hand = []
        self.assertEqual(game1.get_winner(), None)