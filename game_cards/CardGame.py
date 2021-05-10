from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards


class CardGame(Player, DeckOfCards):

    def __init__(self, name1, name2, num_of_cards=10):
        self.deck = DeckOfCards()
        if type(name1) != str:
            player1 = "player1"
        else:
            player1 = name1
        if type(name2) != str:
            player2 = "player2"
        else:
            player2 = name2
        if type(num_of_cards) == int:
            if 0 <= num_of_cards <= 26:
                num = num_of_cards
            else:
                num = 10
        else:
            num = 10
        self.players = [Player(player1, num), Player(player2, num)]
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

    def get_winner(self):
        if len(self.players[0]._Player__hand) > len(self.players[1]._Player__hand):
            self.__started = False
            return self.players[1]
        elif len(self.players[0]._Player__hand) < len(self.players[1]._Player__hand):
            self.__started = False
            return self.players[0]
        else:
            self.__started = False
            return
