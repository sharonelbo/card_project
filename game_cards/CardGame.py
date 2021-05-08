from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards

class CardGame(Player, DeckOfCards):

    def __init__(self, name1, name2, num_of_cards=10):
        self.deck = DeckOfCards()
        self.players = [Player(name1, num_of_cards), Player(name2, num_of_cards)]
        self.__started = False

    def __repr__(self):
        return f"{self.players[0]}\n{self.players[1]}"

    def __str__(self):
        return f"{self.players[0]}\n{self.players[1]}"

    def new_game(self):
        if not self.__started:
            self.deck.shuffle()
            self.players[0].set_hand(self.deck)
            self.players[1].set_hand(self.deck)
            self.__started = True
        else:
            print("Error, the game already started")
            return

    def get_winner(self):
        if self.players[0].get_hand() > self.players[1].get_hand():
            return self.players[1]
        elif self.players[1].get_hand() > self.players[0].get_hand():
            return self.players[0]
        else:
            return


